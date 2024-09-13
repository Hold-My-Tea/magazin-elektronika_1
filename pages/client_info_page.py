from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #### Locators
    father_name = "//input[@name='fio_pname']"
    last_name = "//input[@name='fio_sname']"
    phone_number = "//div/ul/li/input[@name='phone']"
    self_delivery = "(//label[@data-delivery-date='0'])[1]"
    cash_or_card = "(//label[@class='noneactive'])[3]"
    agreement_button = "(//label[@class='agreement__label'])[1]"
    continue_button = "//input[@value='Оформить заказ']"

    ### Getters

    def get_father_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.father_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_self_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.self_delivery)))

    def get_cash_or_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cash_or_card)))

    def get_agreement_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agreement_button)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    ### Actions

    def input_father_name(self, father_name):
        self.get_father_name().send_keys(father_name)
        print("Input father name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input phone_number")

    def checkbox_self_delivery(self):
        self.get_self_delivery().click()
        print("Checkbox self delivery")

    def checkbox_cash_or_card(self):
        self.get_cash_or_card().click()
        print("Checkbox cash or card")
        self.driver.execute_script("window.scrollTo(0, 700)")

    def checkbox_agreement_button(self):
        self.get_agreement_button().click()
        print("Checkbox agreement button")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")


    ### Methods


    def input_info(self):
        self.get_current_url()
        self.input_father_name("Ivanovna")
        self.input_last_name("Petrova")
        self.input_phone_number("+7 (999) 999 99-99")
        self.checkbox_self_delivery()
        self.checkbox_cash_or_card()
        self.checkbox_agreement_button()
        self.click_continue_button()





