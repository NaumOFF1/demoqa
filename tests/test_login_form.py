import time
from pages.form_page import Form_page


def test_login_form(browser):
    form_page = Form_page(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page. last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('1111111111111')
    time.sleep (2)
    form_page.btn_submit.click_force()
    time.sleep (2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

    form_page.hobbies_sports_radio.click_force()
    form_page.current_address.send_keys('Пошли гулять')
    form_page.current_address.clear()
    time.sleep(2)

def test_login_form(browser):
    form_page = Form_page(browser)

    form_page.visit()
    form_page.selector_state.select_input('Uttar Pradesh')
    form_page.selector_city.select_input('Merrut')