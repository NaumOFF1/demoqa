from pages.alerts_page import AlertsPage
import time

def test_allert(browser):
    alerts_page = AlertsPage(browser)

    alerts_page.visit()
    assert not alerts_page.alert()

    alerts_page.alertButton.click()
    time.sleep(2)
    assert alerts_page.alert()

def test_alert_text(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accept()
    assert not alert_page.alert()

def test_alert_text(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'
