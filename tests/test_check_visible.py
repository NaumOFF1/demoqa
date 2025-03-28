from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_visible_btn_slider(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    elements_page.btn_sidebar_elements.click()
    time.sleep(3)
    assert elements_page.btn_sidebar_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_checkbox.visible()
    elements_page.btn_sidebar_elements.click()
    time.sleep(3)
    assert not elements_page.btn_sidebar_checkbox.visible()