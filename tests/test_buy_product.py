import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

@pytest.mark.order(2)
def  test_buy_product_1(set_up):
     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

     print('Start test 1')

     login = LoginPage(driver)
     login.authorization()

     mp = MainPage(driver)
     mp.select_products_1()

     cp = CartPage(driver)
     cp.product_confirmation()

     cip = ClientInfoPage(driver)
     cip.input_info()

     fp = FinishPage(driver)
     fp.finish()

     print("Finish test 1")
     time.sleep(5)
     driver.quit()

@pytest.mark.order(1)
def test_buy_product_2(set_up):
     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

     print('Start test 2')

     login = LoginPage(driver)
     login.authorization()

     mp = MainPage(driver)
     mp.select_products_2()

     cp = CartPage(driver)
     cp.product_confirmation()

     cip = ClientInfoPage(driver)
     cip.input_info()

     fp = FinishPage(driver)
     fp.finish()

     print("Finish test 2")
     time.sleep(10)
     driver.quit()
