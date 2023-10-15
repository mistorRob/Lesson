def test_add_to_cart_button_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_to_cart_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_to_cart_button.is_displayed()
