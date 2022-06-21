from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import *
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Firefox()

urls = ['https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/','https://www.amazon.com/AMD-Ryzen-3600X-12-Thread-Processor/dp/B07SQBFN2D/', 'https://www.amazon.com/dp/B09FWYK5M9/']

def get_price(URL):
    driver.get(URL)
    name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text   

    try:
        driver.get(URL)
        element = driver.find_element_by_class_name('twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
        return (f'\n{name}\nCosts:{price}\n')
        
    except NoSuchElementException:
        try:
          element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
          price = element.get_attribute('innerHTML')
          return (f'\n{name}\nCosts:{price}\n')
        except NoSuchElementException:
            print("Error finding element")
            pass

    driver.quit()
    

def get_sale_percentage(URL):
    driver.get(URL)
    name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text   

    try:
        driver.get(URL)
        element = driver.find_element_by_class_name('twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
        return (f'\n{name}\nCosts:{price}\n')
        
    except NoSuchElementException:
        try:
          element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
          price = element.get_attribute('innerHTML')
          return (f'\n{name}\nCosts:{price}\n')
        except NoSuchElementException:
            print("Error finding element")
            pass
    
    driver.quit()


def get_discount_number(URL):
    driver.get(URL)
    name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text   

    try:
        driver.get(URL)
        element = driver.find_element_by_class_name('twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
        return (f'\n{name}\nCosts:{price}\n')
        
    except NoSuchElementException:
        try:
          element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
          price = element.get_attribute('innerHTML')
          return (f'\n{name}\nCosts:{price}\n')
        except NoSuchElementException:
            print("Error finding element")
            pass

    driver.quit()


def return_lowest_price(AMAZONURL, NEWEGGURL, BESTURL):
   """  driver.get(URL)
    name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text   

    try:
        driver.get(URL)
        element = driver.find_element_by_class_name('twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
        return (f'\n{name}\nCosts:{price}\n')
        
    except NoSuchElementException:
        try:
          element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
          price = element.get_attribute('innerHTML')
          return (f'\n{name}\nCosts:{price}\n')
        except NoSuchElementException:
            print("Error finding element")
            pass
    
    driver.quit() """

