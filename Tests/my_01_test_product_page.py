from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

""" Открываем браузер Chrome"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

"""" Открываем браузер Chrome"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

"""Задаём переменную для ссылки на страницу сайта"""
#test_site_name = "http://tutorialsninja.com/demo/index.php?route=product/product&amp;product_id=42"
test_site_name = "https://yandex.ru/"

start_time = time.time()
driver.get(test_site_name)

finish_time = time.time()

test_time = float(round((finish_time - start_time), 3))
if test_time < 8:
    print(f'Сайт открылся за {test_time} секунды. ТЕСТ ПРОШЁЛ')
else:
    print(f'Сайт не открылся. ТЕСТ НЕ ПРОШЁЛ')

pass
driver.close()
