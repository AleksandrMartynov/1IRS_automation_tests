from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

test_site_name = "http://54.183.112.233/index.php?route=product/search" #Удалить позже

start_time = time.time()
driver.get(test_site_name) #Удалить позже
"""Проверка страницы ПОИСКа на сайте"""  #Удалить позже
search_site_page: WebElement = driver.find_element(By.TAG_NAME, 'h1')
site_page_test = "Search"
if site_page_test == search_site_page.text:
    print("Мы на странице поиска товаров.")
else:
    print("Мы НЕ на странице поиска товаров.")


"""1 Поиск поля 'apple' в строке поиска"""
search_fild = driver.find_element(By.ID, 'input-search')
search_fild.send_keys('apple')
button_search = driver.find_element(By.CLASS_NAME, 'btn-primary')
button_search.click()
""" Как дальше искать, если у нас товар может появляться в любом месте, если их несколько. По каким критериям искать?????"""
""" Как дальше искать, если у нас товар может появляться в любом месте, если их несколько. По каким критериям искать?????"""
""" Как дальше искать, если у нас товар может появляться в любом месте, если их несколько. По каким критериям искать?????"""


""" Тут написать возврат на предыдущую страницу ===> Back или Очистить поле поиска"""

"""2 Поиск поля 'sony' в строке поиска"""
search_fild = driver.find_element(By.ID, 'input-search')
search_fild.send_keys('sony')
button_search = driver.find_element(By.CLASS_NAME, 'btn-primary')
button_search.click()

""" Тут написать возврат на предыдущую страницу ===> Back или Очистить поле поиска"""

"""3 Поиск поля 'nokia' в строке поиска"""
search_fild = driver.find_element(By.ID, 'input-search')
search_fild.send_keys('sony')
button_search = driver.find_element(By.CLASS_NAME, 'btn-primary')
button_search.click()


"""4 Поиск по 4му условию ТК в строке поиска"""
search_fild = driver.find_element(By.ID, 'input-search')
search_fild.send_keys('stunning')
# Ставим галочку на критерии поиска под полем ПОИСК
product_description = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[1]/label/input")
product_description.click()
button_search = driver.find_element(By.CLASS_NAME, 'btn-primary')
button_search.click()








finish_time = time.time()
test_time = float(round((finish_time - start_time), 4))
print(f'Время открытия сайта {test_time} секунд(ы).')
driver.close()
