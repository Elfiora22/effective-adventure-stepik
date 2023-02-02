import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(LINK)
    time.sleep(5)

    btn = browser.find_element(By.CSS_SELECTOR, "form#add_to_basket_form > .btn.btn-add-to-basket.btn-lg.btn-primary")
    
    assert True, "Button add_to_basket is found!"
    print("\n Good assert makes the test look beautiful")