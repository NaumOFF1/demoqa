from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa

def test_navigation(browser):
    demoqa = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demoqa.visit()
    demoqa.btn_elements.click()
    demoqa.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()
