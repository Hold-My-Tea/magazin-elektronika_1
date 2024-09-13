import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains



class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # #### Locators
    select_product_1 = "/html/body/main/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/form/div[2]/div/div[2]"
    cart = "//div[@class='c-cart__small--icon']"
    catalog = "//div[@class='c-nav__text c-menu__text']"
    optoehlektronika = "//div/a[@href='https://magazin-elektronika.ru/optoehlektronika-7']"
    svetodiody = "//div/a[@href='https://magazin-elektronika.ru/optoehlektronika-7/svetodiody-701']"
    main_page_button = "//a[@title='«Магазин Электроника»']"
    sort_by = "//select[@id='sorter']"
    first_cheap = "//option[@value='price_course|-1']"
    slider_2 = "(//span[@tabindex='0'][2])"
    filter_button = "//input[@class='filter-btn']"
    amount_input_1 = "(//input[@name='amount_input'])[1]"
    buy_button_1 = "(//div[@class='c-buy__buttons'])[1]"
    about_us = "//span[@class='c-nav__text c-menu__text']"
    our_history_link ="(//div[@class='c-nav__text c-menu__text'])[2]"




    ### Getters
    def get_select_product_1(self):
          return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
          return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_catalog(self):
          return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_main_page_button(self):
          return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_page_button)))

    def get_optoehlektronika(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.optoehlektronika)))

    def get_svetodiody(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.svetodiody)))

    def get_sort_by(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by)))

    def get_first_cheap(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_cheap)))

    def get_slider_2(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_2)))
    def get_filter_button(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_amount_input_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amount_input_1)))

    def get_buy_button_1(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button_1)))

    def get_about_us(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_us)))

    def get_our_history_link(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.our_history_link)))


    ### Actions

    def click_select_product_1(self):
          self.get_select_product_1().click()
          print("Click select product 1")

    def click_cart(self):
         self.driver.execute_script("window.scrollTo(0, 0);")
         self.get_cart().click()
         print("Click cart")

    def click_main_page_button(self):
          self.get_main_page_button().click()
          print("Click main page button")

    def click_catalog(self):
          self.get_catalog().click()
          print("Click catalog")

    def click_optoehlektronika(self):
         self.get_optoehlektronika().click()
         print("Click optoehlektronika")

    def click_svetodiody(self):
        self.get_svetodiody().click()
        print("Click svetodiody")

    def click_sort_by(self):
        self.get_sort_by().click()
        print("Click sort by")

    def click_first_cheap(self):
        self.get_first_cheap().click()
        print("Click first cheap")

    def click_slider_2(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider_2()).move_by_offset(-50, 0).release().perform()
        print("Click slider 2")

    def click_filter_button(self):
        self.get_filter_button().click()
        print("Click filter button")

    def input_amount_input_1(self):
        self.get_amount_input_1().send_keys(Keys.CONTROL + "a")
        time.sleep(3)
        self.get_amount_input_1().send_keys('4')
        print("Input amount input 1")

    def click_buy_button_1(self):
        self.get_buy_button_1().click()
        print("Click buy button 1")

    def click_about_us(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_about_us()).perform()
        print("Click about us")

    def click_our_history_link(self):
        self.get_our_history_link().click()
        print("Click our history link")




    ### Methods

    def select_products_1(self):
        self.click_main_page_button()
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_catalog()
        self.click_optoehlektronika()
        self.click_svetodiody()
        self.click_slider_2()
        self.click_filter_button()
        self.click_sort_by()
        self.click_first_cheap()
        self.input_amount_input_1()
        self.click_buy_button_1()
        self.click_cart()

    def select_our_history(self):
        self.get_current_url()
        self.click_about_us()
        self.click_our_history_link()
        self.assert_url('https://magazin-elektronika.ru/about/nasha-istoriya')


    # def select_optoehlektronika(self):
    #      self.get_current_url()
    #     self.click_menu()
    #     self.click_link_sweets_with_alco()
    #     self.assert_url('https://www.alenka.ru/catalog/konfety/konfety_s_alkogolem/')




