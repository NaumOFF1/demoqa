from pages.modal_dialogs_page import Modal_Dialog_Page
from pages.demoqa import DemoQa

def test_modal_dialogs(browser):
    modal_dialogs = Modal_Dialog_Page(browser)

    modal_dialogs.visit()
    assert modal_dialogs.uniq_locator_btn_third.check_count_elements(5)

def test_navigation_modal(browser):
    modal_dialogs = Modal_Dialog_Page(browser)
    demoqa = DemoQa(browser)

    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.btn_icon.click()
    browser.back()
    browser.set_window_size(height=900, width=400)
    browser.forward()
    assert demoqa.equal_url()
    assert demoqa.get_title() == 'DEMOQA'
    browser.set_window_size(height=1000, width=1000)
