"""from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/cats.html')
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, "button")

finally:
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    button = browser.find_element(By.XPATH, '//button[@id="book"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button) # argumentS!
    price = WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
   )
    button.click()


    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text

    def calc(x):
        return math.log(abs(12*math.sin(int(x))))

    y = calc(x)

    text_area = browser.find_element(By.NAME, 'text')
    text_area.send_keys(y)

    buttton1 = browser.find_element(By.CSS_SELECTOR, '[type= "submit"]').click()

    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    alert.accept()

finally:
    browser.quit()

