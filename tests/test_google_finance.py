import unittest
from pages.google_finance_page import GoogleFinancePage
from utils.setup import BaseTest


class GoogleFinanceTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.google_finance_page = GoogleFinancePage(self.driver)

        # Load google finance page
        self.load_page()

        # Verify the page loads
        self.google_finance_page.verify_page_loaded()
        self.test_data_set = {"NFLX", "MSFT", "TSLA"}

    def test_compare_stock_symbols(self):
        # Stock symbols from the UI
        ui_stock_symbols = set(self.google_finance_page.get_stock_symbols())

        for symbol in self.test_data_set:
            if symbol in ui_stock_symbols:
                print(f"Stocks in UI - {symbol} ")
            else:
                print(f"Stocks NOT in UI - {symbol}")

        # Display stock symbols not in given data
        symbols_not_in_test_data = ui_stock_symbols - self.test_data_set
        print(f"Step 5. Stock symbols in UI but not in given test data: {symbols_not_in_test_data}")

        # Display stock symbols not in UI
        symbols_not_in_ui = self.test_data_set - ui_stock_symbols
        print(f"Step 6. Stock symbols in given test data but not in UI: {symbols_not_in_ui}")

    def test_ui_stocks_not_in_given_data(self):
        # Stock symbols from the UI
        ui_stock_symbols = set(self.google_finance_page.get_stock_symbols())

        # Display stock symbols not in given data
        symbols_not_in_test_data = ui_stock_symbols - self.test_data_set
        print(f"TestCase-5. Stock in UI but not in test data: {symbols_not_in_test_data}")

    def test_given_stocks_data_not_in_ui(self):
        # Stock symbols from the UI
        ui_stock_symbols = set(self.google_finance_page.get_stock_symbols())

        # Display stock symbols not in UI
        symbols_not_in_ui = self.test_data_set - ui_stock_symbols
        print(f"TestCase 6. Stock in test data but not in UI: {symbols_not_in_ui}")


if __name__ == "__main__":
    unittest.main()
