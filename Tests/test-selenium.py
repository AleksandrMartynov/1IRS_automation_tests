# Подключаем библиотеку Селениум.
# Потому что в самом языке Python ничего про веб-тестирование нет.
# Селениум нужно скачать, установить, и подключить через import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


""" Класс Service служит для запуска и остановки ChromeDriver"""
service = Service(executable_path = "C:\\Users\\Aleksandr\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe")

# Класс Chrome уже служит для того, чтобы управлять всеми возможностями браузера.
driver = webdriver.Chrome(service=service)

# Открыть браузер на нужной странице
driver.get('https://www.google.com')

pass
#driver.quit()