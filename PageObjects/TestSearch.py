from selenium.webdriver.remote.webelement import WebElement

"""
1. Импортировать из класса 'BrowserSettings' метод 'import_selenium_tool'
"""

test_site_name = "http://54.183.112.233/index.php?route=product/search"

"""
2. Функция проверки что мы на странице"""

def check_site_page(str: IND, str: name_IND ):
    search_site_page: WebElement = driver.find_element(By.TAG_NAME, 'h1')
    site_page_test = "Search"
    if site_page_test == search_site_page.text:
        print("Мы на странице поиска товаров.")
    else:
        print("Мы НЕ на странице поиска товаров.")

