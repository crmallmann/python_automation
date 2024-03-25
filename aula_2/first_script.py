from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get("https://www.uol.com.br")

browser.maximize_window()

sleep(5)

titulo = browser.title

print(titulo)

browser.quit()