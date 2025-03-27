from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


# def test_check_text_footer(browser):
#     demo_qa_page = DemoQa(browser)

#     demo_qa_page.visit()
#     assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

# def test_check_text_center_elements(browser):
#     demo_qa_page = DemoQa(browser)
#     elements_page = ElementsPage(browser)

#     demo_qa_page.visit()
#     demo_qa_page.btn_elements.click()
#     assert elements_page.text_center_element.get_text() == 'Please select an item from left to start practice.'

# def test_page_elements(browser):
#     elements_page = ElementsPage(browser)

#     elements_page.visit()
#     assert elements_page.footer_icon.exist()
#     assert elements_page.btn_sidebar_elements.exist()
#     assert elements_page.btn_sidebar_textbox.exist()

# def test_exist_btn_slider(browser):
#     elements_page = ElementsPage(browser)

#     elements_page.visit()
#     elements_page.btn_sidebar_elements.click()
#     time.sleep(3)
#     assert elements_page.btn_sidebar_textbox.exist()

