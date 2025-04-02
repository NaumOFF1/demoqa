from pages.webtables_page import WebtablesPage
import time

def test_sort(browser):

    sort_class = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    
    web = WebtablesPage(browser)
    web.visit()

    web.header_table_first_name.click_force()
    assert web.header_table_first_name.get_dom_attribute('class') == sort_class

    web.header_table_last_name.click_force()
    assert web.header_table_last_name.get_dom_attribute('class') == sort_class

    web.header_table_age.click_force()
    assert web.header_table_age.get_dom_attribute('class') == sort_class

    web.header_table_email.click_force()
    assert web.header_table_email.get_dom_attribute('class') == sort_class

    web.header_table_salary.click_force()
    assert web.header_table_salary.get_dom_attribute('class') == sort_class

    web.header_table_departament.click_force()
    assert web.header_table_departament.get_dom_attribute('class') == sort_class




