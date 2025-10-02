# selenium/google_search.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")   # abre maximizado

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 12)

try:
    # 1) Abrir Google
    driver.get("https://www.google.com")

    # 2) Buscar "laptops"
    box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    box.send_keys("laptops")
    box.send_keys(Keys.RETURN)

    # 3) Esperar resultados y dar clic en el primer resultado orgánico
    first_result = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//div[@id='search']//a[h3])[1]")
    ))

    title = first_result.find_element(By.TAG_NAME, "h3").text
    url = first_result.get_attribute("href")
    print(f"➡️ Primer resultado: {title} ({url})")

    first_result.click()

    # 4) Esperar a que cargue la página destino
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
    print(f"✅ Navegación correcta. Página abierta: {driver.title}")

    time.sleep(3)

finally:
    driver.quit()
