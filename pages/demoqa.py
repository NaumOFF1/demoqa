from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class DemoQa(BasePage):

    locator_icon = ("xpath", "/html/body/div[2]/header/a/img")
    locator_btn_elements = ("xpath", "/html/body/div[2]/div/div/div[2]/div/div[1]")


    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)

    def exist_icon(self):
        try:
            self.find_element(*self.locator_icon)
        except NoSuchElementException:
            return False
        return True
    
    def click_on_the_icon(self):
        self.find_element(*self.locator_icon).click()

    def click_on_the_btn(self):
        self.find_element(*self.locator_btn_elements).click()

    def equal_url(self):
        if self.get_url == self.base_url:
            return True
        return False


