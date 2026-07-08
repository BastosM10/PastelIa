from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("Iniciando WhatsApp...")

opcoes = Options()

opcoes.add_argument("--start-maximized")
opcoes.add_argument("--disable-extensions")
opcoes.add_argument("--disable-gpu")
opcoes.add_argument("--no-sandbox")
opcoes.add_argument("--disable-dev-shm-usage")
opcoes.add_argument("--remote-debugging-port=9222")
opcoes.add_argument("--user-data-dir=C:/PastelIA/whatsapp_sessao")

navegador = webdriver.Chrome(options=opcoes)

navegador.get("https://web.whatsapp.com")

print("WhatsApp Web aberto. Escaneie o QR Code se aparecer.")

while True:
    time.sleep(10)