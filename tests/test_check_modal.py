from pages.modal_dialogs_page import Modal_Dialog_Page
import time

def test_check_modal(browser):

    modal = Modal_Dialog_Page(browser)
    modal.visit()
    modal.page_availability()

    modal.small_button.click_force()
    modal.modal_content.exist()
    modal.close_small_modal_button.click_force()
    time.sleep(2)
    modal.page_availability()

    modal.large_button.click_force()
    modal.modal_content.exist()
    modal.close_large_modal_button.click_force()
    modal.page_availability()