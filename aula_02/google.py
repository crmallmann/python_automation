from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicialize o WebDriver (assumindo que você está usando o Chrome)
driver = webdriver.Chrome()

try:
    # Abra o Google
    driver.get("https://www.google.com")

    # Aguarde até que a página carregue completamente
    time.sleep(2)

    # Encontre a barra de pesquisa pelo id
    search = driver.find_element(By.ID, "APjFqb")

    # Digite "cypress" na barra de pesquisa e pressione Enter
    search.send_keys("python")
    search.send_keys(Keys.RETURN)

    # Aguarde para ver os resultados
    time.sleep(5)

finally:
    # Feche o navegador
    driver.quit()
