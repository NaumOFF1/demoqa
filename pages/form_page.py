from pages.base_page import BasePage
from components.components import WebElement

class Form_page(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.hobbies_sports_radio = WebElement(driver, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.current_address = WebElement(driver, '#currentAddress')
        self.form_novalidate = WebElement(driver, '#userForm')

        self.selector_state = WebElement(driver, '#react-select-3-input')
        self.selector_city = WebElement(driver, '#react-select-4-input')