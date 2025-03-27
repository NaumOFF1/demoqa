from pages.base_page import BasePage
from components.components import WebElement

class Accordian_page(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

        self.section_content_first = WebElement(driver, '#section1Content > p')
        self.section_content_second_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_content_second_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_content_third = WebElement(driver, '#section3Content > p')
        self.btn_setion_heading = WebElement(driver, '#section1Heading')
