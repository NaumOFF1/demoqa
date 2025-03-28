from pages.text_box import Text_box_page
from pages.form_page import Form_page
import time

full_name: str = 'Наумов Данила'
current_adress: str = 'Тестовая среда'

def test_text_box(browser):
    text_box = Text_box_page(browser)

    text_box.visit()
    text_box.full_name.send_keys(full_name)
    text_box.current_adress.send_keys(current_adress)
    time.sleep(2)
    text_box.btn_submit.click_force()

    
    assert 'Name:' + full_name in text_box.introduced.get_text()
    assert 'Current Address :' + current_adress in text_box.introduced.get_text()


