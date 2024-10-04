import os

from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleFinancePage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = finance
        # self.config = self.load_config()

    # def load_config(self):
    #     config = {}
    #
    #     script_dir = os.path.dirname(os.path.abspath('\Take Home Exercise'))
    #     file_path = os.path.join(script_dir, 'data.txt')
    #
    #     with open(file_path, 'r') as file:
    #         for line in file:
    #             if "=" in line:
    #                 key, value = line.strip().split('=', 1)
    #                 config[key] = value
    #     return config
    #
    # def load_page(self):
    #     url = self.config.get('url')
    #     self.driver.get(url)

    def verify_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Google Finance"))

    def get_stock_symbols(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.locator.STOCK_SYMBOLS))
        stock_elements = self.driver.find_elements(*self.locator.STOCK_SYMBOLS)
        stock_symbols = [element.text for element in stock_elements]
        return stock_symbols
