from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import denemesonuc.models


def fetch(
    driver: WebDriver,
    ad: str,
    no: int,
    duzey: int,
    sehir: str,
    ilce: str,
    kurum: str,
    deneme: denemesonuc.models.DenemeLogin,
    starting_div: int = 8,
    naming_aliases: dict[str, str] = {},
) -> denemesonuc.models.DenemeResult:
    """### denek ve deneme bilgileriyle yeni tip deneme sonuçlarını çeker

    returns DenemeResult if successful
    raises DenekNotFound if denek did not take the test
    raises RunTimeError if element with text not found on login page"""

    ret = denemesonuc.models.DenemeResult()

    if deneme.logout_url:
        driver.get(deneme.logout_url)

    driver.get(deneme.url)

    driver.find_element("id", "select2-gt_ogrencino_sinifcombo-container").click()
    Select(driver.find_element("id", "select2-gt_ogrencino_sinifcombo-results")).select_by_visible_text(str(duzey) + ".Sınıf")

    driver.find_element("id", "select2-gt_ogrencino_ilcombo-container").click()
    Select(driver.find_element("id", "select2-gt_ogrencino_ilcombo-results")).select_by_visible_text(sehir)

    driver.find_element("id", "select2-gt_ogrencino_ilcecombo-container").click()
    Select(driver.find_element("id", "select2-gt_ogrencino_ilcecombo-results")).select_by_visible_text(ilce)

    driver.find_element("id", "select2-gt_ogrencino_kurumcombo-container").click()
    Select(driver.find_element("id", "select2-gt_ogrencino_kurumcombo-results")).select_by_visible_text(kurum)

    ogrnoinp = driver.find_element("id", "gt_ogrencino_ogrnoedit")
    ogrnoinp.send_keys(str(no))

    # if it exists, type value
    for i in ("gt_ogrencino_adsoyadedit", "gt_ogrencino_adedit"):
        try:
            adinp = driver.find_element("id", i)
            adinp.send_keys(ad)
        except NoSuchElementException:
            pass

    driver.find_element("id", "gt_ogrencino_girisbtn").submit()

    try:
        WebDriverWait(driver, 6).until(
            EC.presence_of_element_located(("xpath", "/html/body/section/div/div[1]/div/div/h6[2]"))
        )
    except TimeoutException as e:
        raise TimeoutException("denek probably did not take the test") from e

    root = driver.find_element("xpath", "/html/body/section")
    li = root.find_elements("tag name", "a")
    for i in li:
        if i.text == deneme.deneme_adi:
            i.click()
            break
    else:
        raise denemesonuc.models.DenekNotFound("denek did not take the test")

    # at data page

    document = "/html/body/section"

    derece_head = f"{document}/div[1]/div[5]/div/div/div/"
    d_sinif = int(
        driver.find_element("xpath", f"{derece_head}/div[2]").text
    )  # /html/body/section/div[1]/div[5]/div/div/div/div[2]
    d_kurum = int(
        driver.find_element("xpath", f"{derece_head}/div[3]").text
    )  # /html/body/section/div[1]/div[5]/div/div/div/div[3]
    d_il = int(driver.find_element("xpath", f"{derece_head}/div[5]").text)
    d_genel = int(driver.find_element("xpath", f"{derece_head}/div[6]").text.split("\n")[0])
    ret.drc = denemesonuc.models.DenemeDerece(d_sinif, d_kurum, d_il, d_genel)

    ret.sinif = (
        driver.find_element("xpath", f"{document}/div/div[1]/div/div/h5")
        .text.replace("-", "")  # 9larda "-9A" gibi, diğer sınıflarda "11A" gibi gözüküyor o yüzden
        .split()[0]
    )  # "12C / 987" gibi.

    ret.puan = float(
        driver.find_element(
            "xpath", f"/html/body/section/div[1]/div[3]/div/div/div/div[2]"
        ).text.replace(",", ".")
    )

    ul = driver.find_element("xpath", f"{document}/div[1]")
    li = ul.find_elements("tag name", "div")

    i = starting_div - 1
    available_heads = {}
    while True:
        i += 1
        try:
            driver.find_element("xpath", f"{document}/div[1]/div[{i}]")
        except NoSuchElementException:
            break

        try:
            b = driver.find_element("xpath", f"{document}/div[1]/div[{i}]/div/div")
            c = driver.find_element("xpath", f"{document}/div[1]/div[{i+1}]/div[2]/div/div")
        except NoSuchElementException:
            continue

        if c.find_elements("tag name", "h3"):
            h = "3"
        elif c.find_elements("tag name", "h2"):
            h = "2"
        elif c.find_elements("tag name", "h5"):
            h = "5[2]"
        else:
            continue

        available_heads[b.text] = denemesonuc.models.DersSonuc(
            int(
                driver.find_element(
                    "xpath", f"{document}/div[1]/div[{i+1}]/div[2]/div/div/h{h}"
                ).text
            ),
            int(
                driver.find_element(
                    "xpath", f"{document}/div[1]/div[{i+1}]/div[3]/div/div/h{h}"
                ).text
            ),
            int(
                driver.find_element(
                    "xpath", f"{document}/div[1]/div[{i+1}]/div[4]/div/div/h{h}"
                ).text
            ),
            float(
                driver.find_element(
                    "xpath", f"{document}/div[1]/div[{i+1}]/div[5]/div/div/h{h}"
                ).text.replace(",", ".")
            ),
            int(
                driver.find_element(
                    "xpath", f"{document}/div[1]/div[{i+1}]/div[1]/div/div/h{h}"
                ).text
            ),
        )

    ret.genel = available_heads.get(naming_aliases.get("genel", "Toplam"))
    ret.edb = available_heads.get(naming_aliases.get("edb", "TYT Türkçe Testi Toplamı"))
    ret.trh = available_heads.get(naming_aliases.get("trh", "Tarih-1"))
    ret.cog = available_heads.get(naming_aliases.get("cog", "Coğrafya-1"))
    ret.din = available_heads.get(naming_aliases.get("din", "Din Kül. ve Ahl. Bil."))
    ret.mat = available_heads.get(naming_aliases.get("mat", "TYT Matematik Testi Toplamı"))
    ret.fiz = available_heads.get(naming_aliases.get("fiz", "Fizik"))
    ret.kim = available_heads.get(naming_aliases.get("kim", "Kimya"))
    ret.biy = available_heads.get(naming_aliases.get("biy", "Biyoloji"))
    ret.fel = available_heads.get(naming_aliases.get("fel", "Felsefe"))
    ret.sfl = available_heads.get(naming_aliases.get("sfl", "Felsefe (Seçmeli)"))


    return ret
