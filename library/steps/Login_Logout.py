import time
import tempfile
import shutil
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from robot.libraries.BuiltIn import BuiltIn

class Login_Logout:
    def __init__(self):
        self.selib = SeleniumLibrary()
        self.driver = None
        self.temp_dir = None

    @keyword("the user logs-in to the website")
    def the_user_logs_in_to_the_website(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')

        # Create a temp user-data-dir to avoid Chrome session errors
        self.temp_dir = tempfile.mkdtemp()
        options.add_argument(f'--user-data-dir={self.temp_dir}')

        self.driver = webdriver.Chrome(options=options)
        self.selib.register_driver(self.driver, alias="headless_chrome")

        self.selib.go_to("https://www.saucedemo.com/")
        self.selib.input_text("id:user-name", "standard_user")
        self.selib.input_text("id:password", "secret_sauce")
        self.selib.click_button("id:login-button")

    @keyword("the user logs-out from the website")
    def the_user_logs_out_from_the_website(self):
        self.selib.switch_browser("headless_chrome")
        time.sleep(3)
        self.selib.click_element("id:react-burger-menu-btn")
        time.sleep(1)
        self.selib.click_element("id:logout_sidebar_link")
        self.selib.close_browser()

        if self.temp_dir:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            self.temp_dir = None

    @keyword("the user stores the price of the item '${itemName}' into '${itemPrice}'")
    def the_user_stores_the_price_of_the_item_into(self, itemName, itemPrice):
        '''
        Reads the item name from the command line and stores the price into 'itemPrice' variable
        :param itemName: name of the item whose price has to be read is passed through cli
        :param price: Stores the item's price, makes it as a global variable
        '''
        print("Prints the item name", itemName)
        self.selib.switch_browser("headless_chrome")
        self.selib.click_element("xpath=//div[text()='Sauce Labs Backpack']")
