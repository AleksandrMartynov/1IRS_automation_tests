from webdriver_manager import driver
import unittest


class __init__():
    class BrowserSettings:

        def import_selenium_tool(self):
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.common.by import By
            from selenium.webdriver.remote.webelement import WebElement
            from webdriver_manager.chrome import ChromeDriverManager
            import time

            driver = self.webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        def settings_size_window(int: choose_window):
            switcher(choose_window) = {
                0: return driver.set_window_size(1280, 960),
                1: return driver.set_window_size(1440, 1050),
                2: return driver.set_window_size(1600, 1200),
                3: return driver.set_window_size(1920, 1080),
            }
        return driver.set_window_size(800, 600)


        """def time_testing(self) -> float:
            start_time = time.time()
            finish_time = time.time()
            test_time = float(round((finish_time - start_time), 4))
            print(f'Тест прошёл за {test_time} секунд(ы).')"""

        def open_site_url(site_name: str):
            test_site_name = site_name
            driver.get(test_site_name)
            return

        def close_site(self):
            return driver.quit()
