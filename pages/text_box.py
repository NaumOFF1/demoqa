from pages.base_page import BasePage
from components.components import WebElement

class Text_box_page(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.email = WebElement(driver, '#userEmail')
        self.current_adress = WebElement(driver, '#currentAddress')

        self.btn_submit = WebElement(driver, '#submit')

        self.introduced = WebElement(driver, '#output > div')

