from pages.browser_windows_page import BrowserWindows
import time

def test_browser_tab(browser):
    br_tab = BrowserWindows(browser)
    
    br_tab.visit()

    assert len(browser.window_handles) == 1
    br_tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)