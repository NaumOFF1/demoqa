import logging
import requests
class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)
    
    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False
        
    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_title(self):
        return self.driver.title

    def refresh(self):
        self.driver.refresh

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
        
    def page_availability(self):
        url = self.get_url()
        if requests.head(url).status_code != 200:
            return False
        else:
            return True