from datetime import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    #### Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    #### Method assert word

    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print("Word is correct")

    #### Method screenshot
    def get_screenshot(self):
        current_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot.png' + current_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Oksana\\AQA\\magazin-elektronika\\screen\\' + name_screenshot)

    #### Method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Url is correct")
