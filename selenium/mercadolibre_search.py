# selenium/mercadolibre_search.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# Evita headless para reducir challenges anti-bot
# options.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)


def click_if_present(selectors, timeout=4):
    for by, sel in selectors:
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, sel))).click()
            return True
        except Exception:
            continue
    return False


try:
    # 1) Ir a MercadoLibre MX
    driver.get("https://www.mercadolibre.com.mx/")

    # 2) Cerrar cookies si aparece (varios textos/ids posibles)
    click_if_present([
        (By.XPATH, "//button[normalize-space()='Entendido']"),
        (By.XPATH,
         "//button[contains(.,'Aceptar') and contains(.,'cookies')]"),
        (By.CSS_SELECTOR, "button#newCookieDisclaimerButton, button#onetrust-accept-btn-handler"),
    ], timeout=6)

    # 3) Localizar el buscador (probamos varios selectores comunes)
    search_box = None
    for by, sel in [
        # buscador principal en home
        (By.ID, "cb1-edit"),
        # nombre del campo de búsqueda
        (By.NAME, "as_word"),
        (By.CSS_SELECTOR, "input[aria-label*='Buscar']"),
        (By.CSS_SELECTOR, "form[action*='listado'] input[type='text']"),
    ]:
        try:
            search_box = wait.until(
                EC.visibility_of_element_located((by, sel)))
            break
        except Exception:
            continue

    if not search_box:
        # Si MercadoLibre muestra un challenge anti-bot, permitimos intervención manual
        if "verify" in driver.page_source.lower() or "robot" in driver.page_source.lower():
            input(
                "⏸️ Parece haber un challenge anti-bot. Resuélvelo y presiona Enter para continuar...")
            # Reintenta encontrar el buscador
            search_box = wait.until(
                EC.visibility_of_element_located((By.ID, "cb1-edit")))
        else:
            raise Exception("No se encontró el campo de búsqueda.")

    # 4) Buscar "laptops"
    search_box.clear()
    search_box.send_keys("laptops")
    search_box.send_keys(Keys.RETURN)

    # 5) Esperar resultados (distintos layouts posibles)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".ui-search-results, .ui-search-layout, ol.ui-search-layout")))
    result_items = driver.find_elements(
        By.CSS_SELECTOR, ".ui-search-result__wrapper, .ui-search-layout__item, li.ui-search-layout__item")

    visible = [el for el in result_items if el.is_displayed()]
    print(f"✅ Resultados visibles para 'laptops': {len(visible)}")

    # (Opcional) Tomar el título del primer resultado
    try:
        first_title = driver.find_element(
            By.CSS_SELECTOR, ".ui-search-item__title, h2.ui-search-item__title").text
        print(f"📝 Primer resultado: {first_title}")
    except Exception:
        pass

    time.sleep(2)  # para ver el estado final

finally:
    driver.quit()
