import time
import pytest
from pages.demoqa import DemoQa
from pages.accordian_page import Accordion
from pages.alerts_page import Alerts
from pages.browser_windows_page import BrowserTab

@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'

