import select
import os

import serial
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from robot.api.deco import keyword
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AddToCart:
    # Set up and start a virtual display
    display = Display(visible=0, size=(1920, 1200))
    display.start()
    # Set Chrome options
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--remote-debugging-port=9222')
    # Adding stuff for capturing the screen
    chrome_options.add_argument("window-size=1980,960")
    chrome_options.add_argument("screenshot")

    # Initialize ChromeDriver using WebDriver Manager
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),  # Automatically manages the driver version
        options=chrome_options
    )
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.implicitly_wait(25)

    @keyword("the user stores the price of the item '${itemName}' into '${itemPrice}'")
    def the_user_stores_the_price_of_the_item_into(self, itemName, itemPrice):
        '''
        Reads the item name from the command line and stores the price into 'itemPrice' variable
        :param itemName: name of the item whose price has to be read is passed through cli
        :param price: Stores the item's price, makes it as a global variable
        '''
        print("Prints the item name", itemName)

    @keyword("the user writes the item '${itemName} and price '${itemPrice}' into the file")
    def the_user_writes_the_item_and_price_into_the_file(self, itemName, itemPrice, fileName):
        '''
        Writes the item's name and price into the given file
        :param itemName: Name of the item, passed through the cli and gets stored into the file
        :param itemPrice: Price of the item, gets stored into the file
        :param fileName: Name of the file into which the items name and price to be stored
        '''
        print("Details", itemName, itemPrice, fileName)
        try:
            with open(fileName, 'w') as fp:
                fp.write(f"{itemName}: {itemPrice}")
        except FileNotFoundError:
            print("File doesn't exist")

    @keyword("the user adds the '${itemName}' to the cart")
    def the_user_adds_the_to_the_cart(self, itemName):
        '''
        Adds the desired item into the cart
        :param itemName: Item name which has to be added into the cart
        '''
        print("Cart", itemName)

    @keyword("the user stores the cart item into")
    def the_user_stores_the_cart_item_into(self, cartItem):
        '''
        Reads back the cart item name for further compariing whether correct item was added to the cart
        Verification shall be taken in other step (handled in robot in-built keyword)
        :param cartItem: Cart item name is retrieved
        '''
        print("cart", cartItem)