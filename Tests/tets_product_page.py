from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

test_site_name = "http://54.183.112.233/index.php?route=product/product&product_id=42"

start_time = time.time()
driver.get(test_site_name)

"""1.Проверка первого поля Apple Cinema"""
name_apple30_text: WebElement = driver.find_element(By.TAG_NAME, 'h1')
name_apple30_test = 'Apple Cinema 30\"'
if name_apple30_test == name_apple30_text.text:
    print("Поле Apple Cinema совпадает.")
else:
    print("Поле Apple Cinema НЕ совпадает.")

"""2.Проверка второго поля Apple Cinema"""
brand_name: WebElement = driver.find_element(By.LINK_TEXT, 'Apple')
brand_name_test = 'Apple'
if brand_name_test == brand_name.text:
    print("Поле брэнд Apple совпадает.")
else:
    print("Поле брэнд Apple НЕ совпадает.")

"""3.Проверка третьего поля Product 15"""
product_name: WebElement = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul[1]/li[2]')
product_name_test = 'Product Code: Product 15'
if product_name_test == product_name.text:
    print("Поле Product Code совпадает.")
else:
    print("Поле Product Code НЕ совпадает.")

"""4.Проверка четвёртого поля Price $110"""
price_name: WebElement = driver.find_element(By.TAG_NAME, 'h2')
price_name_test = '$110.00'
if product_name_test == product_name.text:
    print("Поле Price $110 совпадает.")
else:
    print("Поле Price $110 НЕ совпадает.")

"""
//*[@id="tab-description"]/p[1]/font/font[1]
"""

"""4.Проверка пятого поля Description"""
description_name: WebElement = driver.find_element(By.XPATH, '//*[@id="tab-description"]/p[1]/font/font[1]')
description_name_test = "The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution. Designed specifically for the creative professional, this display provides more space for easier access to all the tools and palettes needed to edit, format and composite your work. Combine this display with a Mac Pro, MacBook Pro, or PowerMac G5 and there's no limit to what you can achieve."
if product_name_test == product_name.text:
    print("Поле Description совпадает.")
else:
    print("Поле Description НЕ совпадает.")








finish_time = time.time()


test_time = float(round((finish_time - start_time), 4))

print(f'Время открытия сайта {test_time} секунд.')

driver.close()