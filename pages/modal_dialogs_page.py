from pages.base_page import BasePage
from components.components import WebElement

class Modal_Dialog_Page(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.uniq_locator_btn_third = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.btn_icon = WebElement(driver, '#app > header > a > img')