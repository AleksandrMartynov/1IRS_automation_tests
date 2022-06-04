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