import time
"""
Данный тест проверяет наличие кнопки "Добавить в корзину". Сразу после того, как
selenium обнаружит кнопку на странице, тест получает текст в переменную button_text
который находится между тегами <button>текст</button> и получает текст, который
находится внутри текга <button> в атрибуте value="" и сравнивает их через assert
"""
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_have_button_add_to_shoppingcart(browser):
    browser.get(link)
    time.sleep(30)
    submit_button = browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    button_text = submit_button.text
    attribute_value_submit_button_text = submit_button.get_attribute("value")
    assert button_text == attribute_value_submit_button_text, "The text between <button> tags and in atrribute value doesn't match"
