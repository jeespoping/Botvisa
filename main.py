from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server


def test_eight_components():
    server = Server('C:/Users/Lopez/Downloads/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    proxy_param = "--proxy-server={0}".format(proxy.proxy)

    options = webdriver.ChromeOptions()
    options.add_argument(proxy_param)
    driver = webdriver.Chrome(options=options)

    proxy.new_har("registro_de_solicitudes")

    driver.get("https://ais.usvisa-info.com/es-co/niv/users/sign_in")

    driver.implicitly_wait(10)

    username_field = driver.find_element(by=By.ID, value='user_email')
    username_field.send_keys("Fernanh96@hotmail.com")

    password_field = driver.find_element(by=By.ID, value='user_password')
    password_field.send_keys("1067952005")

    checkbox = driver.find_element(by=By.CSS_SELECTOR, value=".icheckbox.icheck-item ")

    checkbox.click()

    password_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info-footer")))

    button = driver.find_element(by=By.CSS_SELECTOR, value=".button.primary.small")
    button.click()

    item1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".accordion-item"))
    )

    # Hacer clic en el enlace
    item1.click()

    enlace = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.small.primary.small-only-expanded"))
    )

    enlace.click()

    driver.implicitly_wait(100)

    # Obtiene las entradas capturadas
    har = proxy.har

    # Imprimir las solicitudes y respuestas
    for entry in har['log']['entries']:
        print("URL:", entry['request']['url'])
        print("Método:", entry['request']['method'])
        print("Código de estado:", entry['response']['status'])
        print(entry['response'])
        print("-" * 50)

    server.stop()
    # Cierra el navegador
    driver.quit()

test_eight_components()