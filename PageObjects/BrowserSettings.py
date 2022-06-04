import time
from selenium import driver

class BrawserSettings:

    def import_selenium_tool(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.remote.webelement import WebElement
        from webdriver_manager.chrome import ChromeDriverManager
        import time

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def settings_size_window(self) -> str:
        driver.set_window_size_sxga(1280, 960)
        driver.set_window_size_sxga_pl(1440, 1050)
        driver.set_window_size_uxga(1600, 1200)
        driver.set_window_size_full_hd(1920, 1080)
        return

    def test_work_time(self) -> float:
        start_time = time.time()
        finish_time = time.time()
        test_time = float(round((finish_time - start_time), 4))
        print(f'Тест прошёл за {test_time} секунд(ы).')

    def open_site_page(site_name: str,):
        test_site_name = site_name
        driver.get(test_site_name)
        return

    def close_site(self):
        driver.close()
        return



