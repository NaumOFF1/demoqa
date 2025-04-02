from pages.base_page import BasePage
from components.components import WebElement

class AlertsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alertButton = WebElement(driver, '#alertButton')
        self.confirmButton = WebElement(driver, '#confirmButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.promtBitton = WebElement(driver, '#promtButton')
        self.promtResult = WebElement(driver, '#promtResult')

        self.timeAlertButton = WebElement(driver, '#timerAlertButton')