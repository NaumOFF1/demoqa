import time

from pages.demoqa import DemoQa
from pages.elements_page import ElementPage


def test_go_to_page_elements(browser):
    demoqa_page = DemoQa(browser)
    element_page = ElementPage(browser)

    demoqa_page.visit()
    assert demoqa_page.equal_url()
    demoqa_page.click_on_the_btn()
    assert element_page.equal_url()
