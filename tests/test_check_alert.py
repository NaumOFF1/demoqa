from pages.alerts_page import AlertsPage
import time

def test_check_alert(browser):

    alert = AlertsPage(browser)
    alert.visit()
    alert.timeAlertButton.click_force()
    assert not alert.alert()
    time.sleep(5)
    assert alert.alert()