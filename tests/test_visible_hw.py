from pages.accordian_page import Accordian_page
from pages.base_page import BasePage
import time

def test_visible_accordion(browser):
    page_accord = Accordian_page(browser)

    page_accord.visit()
    assert page_accord.section_content.visible()
    page_accord.btn_setion_heading.click()
    time.sleep(2)
    assert not page_accord.section_content.visible()