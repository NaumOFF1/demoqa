from pages.links_page import LinksPage
import time

def test_windows_tab(browser):

    windows_tab = LinksPage(browser)
    windows_tab.visit()

    assert windows_tab.home_link.get_text() == 'Home'
    assert windows_tab.home_link.get_dom_attribute('href') == 'https://demoqa.com'
     
    windows_tab.home_link.click_force()
    time.sleep(2)
    assert len(browser.window_handles) == 2