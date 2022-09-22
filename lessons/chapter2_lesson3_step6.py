from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    buttton = browser.find_element(By.CSS_SELECTOR, '[class= "trollface btn btn-primary"]').click()
    new_window = browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)


    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text

    def calc(x):
        return math.log(abs(12*math.sin(int(x))))

    y = calc(x)

    text_area = browser.find_element(By.NAME, 'text')
    text_area.send_keys(y)

    buttton1 = browser.find_element(By.CSS_SELECTOR, '[type= "submit"]').click()
    time.sleep(3)

finally:
    browser.quit()



