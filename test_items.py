from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket_exist(browser):
    browser.get(link)

    time.sleep(5) # после открытия страницы ждем для визуальной проверки языка открытой страницы

    assert browser.find_element(By.XPATH, '//button[contains(@class, "btn-add-to-basket")]'), \
        "Button doesn't exist"
