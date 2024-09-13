import time


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


def test_link_sweets_with_alco():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start test')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_our_history()

    print("Finish test")
    time.sleep(10)
    driver.quit()

