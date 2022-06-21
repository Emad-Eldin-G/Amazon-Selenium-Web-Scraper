from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import *
from selenium.common.exceptions import NoSuchElementException
from time import sleep, thread_time
driver = webdriver.Firefox()

def get_price(URL):
    driver.get(URL)
    name  = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text   
    try:
        sleep(2)
        driver.get(URL)
        element = driver.find_element_by_class_name('twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
        return (f'\n{name}\nCosts:{price}\n')
        
    except NoSuchElementException:
        sleep(2)
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
    try:
        sleep(2)
        driver.get(URL)
        element = driver.find_element_by_class_name('a-color-price')
        percentage = element.get_attribute('innerHTML')
        return percentage
        
    except NoSuchElementException:
        sleep(2)
        try:
          element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[3]/td[2]/span[1]')
          percentage = element.get_attribute('innerHTML')
          return percentage
        except NoSuchElementException:
          print("NO SALE")
          pass
    
    driver.quit()


def get_discount_number(URL):
    pass
    """    driver.get(URL)
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
 """

def return_lowest_price(AMAZONURL, NEWEGGURL, BESTURL):
    pass
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

