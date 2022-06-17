from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import *
from time import sleep

options = Options()
options.set_preference('intl.accept_languages', 'en-GB')
driver = webdriver.Firefox(options=options)

driver.get('https://www.amazon.sa/EVGA-220-GA-0750-X1-Modular-Warranty-Compact/dp/B07WW1XF51/')

price = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[7]/div[4]/div[4]/div[10]/div[1]/div[1]/span/span[2]/span[2]').text
name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text

price = int(price.replace(',', ''))

print(f'{name}/n{price}')

driver.quit()
