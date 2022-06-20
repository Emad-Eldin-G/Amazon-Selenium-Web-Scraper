from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import *
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Firefox()

urls = ['https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/','https://www.amazon.com/AMD-Ryzen-3600X-12-Thread-Processor/dp/B07SQBFN2D/', 'https://www.amazon.com/Intel-i7-12700K-Desktop-Processor-Unlocked/dp/B09FXNVDBJ/']

for url in urls:
    driver.get(url)
    name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text   

    try:
        driver.get(url)
        element = driver.find_element_by_class_name('twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
    except NoSuchElementException:
       try:
          element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
          price = element.get_attribute('innerHTML')
       except NoSuchElementException:
              print("Error finding element")
              pass

    price = int(price.replace(',', ''))
    print(f'\n{name}\nCosts:{price}\n')


driver.quit()
