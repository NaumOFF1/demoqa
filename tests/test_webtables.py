from pages.webtables_page import WebtablesPage
import time

def test_1(browser):
    web_tab = WebtablesPage(browser)
    #проверка на отправку незаполненного окна
    web_tab.visit()
    web_tab.btn_add.click_force()
    assert web_tab.modal_content.exist()
    web_tab.btn_submit.click_force()
    assert web_tab.form_novalidate.get_dom_attribute('class') == 'was-validated'
    #заполнение данных
    def input_data():
        web_tab.input_first_name.send_keys('Danila')
        web_tab.input_last_name.send_keys('Naumov')
        web_tab.input_email.send_keys('ffff@gmail.com')
        web_tab.input_age.send_keys('22')
        web_tab.input_salary.send_keys('200000')
        web_tab.input_departament.send_keys('GGGDD')
        time.sleep(3)
        web_tab.btn_submit.click_force()
        time.sleep(3)
    input_data()
    #проверка, что модальное окно закрылось
    assert not web_tab.modal_content.exist()
    #проверка, что в таблицу добавилась новая строка
    assert web_tab.action_buttons_4.exist()
    #проверка на изменение данных
    name = web_tab.first_name_1.get_text()
    web_tab.edit_record_1.click_force()
    web_tab.input_first_name.send_keys('Test')
    web_tab.btn_submit.click_force()
    assert name != web_tab.first_name_1.get_text()
    #проверка на удаление строки
    num_padrow = len(web_tab.padrow_odd.find_elements()) + len(web_tab.padrow_even.find_elements())
    web_tab.delete_record_2.click_force()
    num_padrow_2 = len(web_tab.padrow_odd.find_elements()) + len(web_tab.padrow_even.find_elements())
    assert num_padrow - num_padrow_2 == -1

def test_2(browser):
    web_tab = WebtablesPage(browser)
    #установка предусловий
    web_tab.visit()
    web_tab.select_rows.select_by_value('5')
    #проверка кнопок next/previous
    assert web_tab.btn_Next.get_dom_attribute('disabled')
    assert web_tab.btn_Previous.get_dom_attribute('disabled')
    #добавление 3 строк
    for i in range(3):
        web_tab.btn_add.click_force()
        web_tab.input_first_name.send_keys('Danila')
        web_tab.input_last_name.send_keys('Naumov')
        web_tab.input_email.send_keys('ffff@gmail.com')
        web_tab.input_age.send_keys('22')
        web_tab.input_salary.send_keys('200000')
        web_tab.input_departament.send_keys('GGGDD')
        time.sleep(3)
        web_tab.btn_submit.click_force()
        time.sleep(3)
    #проверка, что появилась вторая страница
    assert web_tab.number_max_page.get_text() == '2'
    #проверка, что кнопка next стала активной
    assert not web_tab.btn_Next.get_dom_attribute('disabled')
    web_tab.btn_Next.click_force()
    #проверка, что мы перешли на 2 страницу таблицы
    assert web_tab.number_active_page.get_dom_attribute('value') == '2'
    web_tab.btn_Previous.click_force()
    #проверка, что мы перешли на 1 страницу таблицы
    assert web_tab.number_active_page.get_dom_attribute('value') == '1'
