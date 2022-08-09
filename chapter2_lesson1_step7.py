from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    img_element = browser.find_element(By.XPATH, '//img[@id="treasure"]')
    x_element = img_element.get_attribute('valuex')
    x = x_element
    print(x)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    textarea = browser.find_element(By.XPATH, '//input[@type="text" and @id = "answer"]')
    textarea.send_keys(y)
    option2 = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    option3 = browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]")
    button.click()
    time.sleep(5)

finally:
    browser.quit()