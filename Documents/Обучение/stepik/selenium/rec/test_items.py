import time


def test_should_be_visible_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(15)
    button = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket')
    btn_text = button.text
    assert btn_text == 'Añadir al carrito', 'Button is not found on the page'
