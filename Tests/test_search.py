from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

test_site_name = "http://54.183.112.233/index.php?route=product/search"

start_time = time.time()
driver.get(test_site_name)

"""1 Поиск поля 'apple' в строке поиска"""
search_fild = driver.find_element(By.ID, 'input-search')
search_fild.send_keys('apple')
button_search = driver.find_element(By.CLASS_NAME, 'btn-primary')
button_search.click()




finish_time = time.time()


test_time = float(round((finish_time - start_time), 4))

print(f'Время открытия сайта {test_time} секунд(ы).')
driver.close()
