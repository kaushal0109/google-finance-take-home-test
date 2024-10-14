from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleFinancePage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = finance

    def verify_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Google Finance"))

    def get_stock_symbols(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.locator.STOCK_SYMBOLS))
        stock_elements = self.driver.find_elements(*self.locator.STOCK_SYMBOLS)
        stock_symbols = [element.text for element in stock_elements]
        return stock_symbols
