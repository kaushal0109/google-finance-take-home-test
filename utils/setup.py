import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)


    def load_config(self):
        config = {}

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'data.txt')

        with open(file_path, 'r') as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
        return config

    def load_page(self):
        url = self.load_config().get('url')
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
