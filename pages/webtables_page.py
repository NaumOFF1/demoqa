from pages.base_page import BasePage
from components.components import WebElement
import time

class WebtablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        #Registration form
        self.btn_submit = WebElement(driver, '#submit') 
        self.modal_content = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.form_novalidate = WebElement(driver, '#userForm')
        self.input_first_name = WebElement(driver, '#firstName')
        self.input_last_name = WebElement(driver, '#lastName')
        self.input_email = WebElement(driver, '#userEmail')
        self.input_age = WebElement(driver, '#age')
        self.input_salary = WebElement(driver, '#salary')
        self.input_departament = WebElement(driver, '#department')
        
        #Base Page
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.select_rows = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.btn_Next = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.btn_Previous = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.number_max_page = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')
        self.number_active_page = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        
        #Table
        self.action_buttons_4 = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(7) > div')
        self.first_name_1 = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.edit_record_1 = WebElement(driver, '#edit-record-1')
        self.delete_record_2 = WebElement(driver, '#delete-record-2')
        self.padrow_odd = WebElement(driver, '//div[@class="rt-tr-group"]//div[@class="rt-tr -padRow -odd"]', 'xpath')
        self.padrow_even = WebElement(driver, '//div[@class="rt-tr-group"]//div[@class="rt-tr -padRow -even"]', 'xpath')
        self.header_table_first_name = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.header_table_last_name = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]', 'xpath')
        self.header_table_age = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]', 'xpath')
        self.header_table_email = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[4]', 'xpath')
        self.header_table_salary = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[5]', 'xpath')
        self.header_table_departament = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[6]', 'xpath')

        self.header_table_locator = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div', 'xpath')