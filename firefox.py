from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Inicia el servidor de browsermob-proxy
server = Server("C:/Users/Lopez/Downloads/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy")
#server = Server("C:/Users/Lopez/Downloads/browsermob-proxy-2.1.3-bin/browsermob-proxy-2.1.3/bin/browsermob-proxy.bat")

server.start()
proxy = server.create_proxy()

# Configura las opciones del navegador con el proxy
proxy_address = "--proxy-server={0}".format(proxy.proxy)
options = Options()
options.add_argument(proxy_address)
options.headless = True

# Inicia el navegador Firefox con las opciones configuradas
driver = webdriver.Firefox(options=options)

# Inicia la captura de las peticiones
proxy.new_har("pagina_web")

# Abre la página web que deseas analizar
driver.get("https://www.google.com/")

# Haz las acciones que deseas en la página (clics, desplazamientos, etc.)


# Pausa la ejecución por 5 segundos
time.sleep(5)


# Detiene la captura y obtiene las peticiones
resultados = proxy.har
print(resultados)
# Imprime las URL de las peticiones y sus respuestas
for entrada in resultados['log']['entries']:
    print(entrada['request']['url'])
    print(entrada['response']['status'])

# Cierra el navegador y detiene el servidor de browsermob-proxy
driver.quit()
server.stop()