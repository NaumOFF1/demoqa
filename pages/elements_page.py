from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_center_element = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        self.footer_icon = WebElement(driver, '#app > header > a > img')
        self.btn_sidebar_elements = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text')
        self.btn_sidebar_textbox = WebElement(driver, '#item-0 > span')
        self.btn_sidebar_checkbox = WebElement(driver, '#item-1 > span')


        