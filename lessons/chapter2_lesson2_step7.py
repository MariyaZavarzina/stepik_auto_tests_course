import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elem_name = browser.find_element(By.NAME, 'firstname')
    elem_name.send_keys('Masha')
    elem_lastname = browser.find_element(By.NAME, 'lastname')
    elem_lastname.send_keys('Zav')
    elem_email = browser.find_element(By.NAME, 'email')
    elem_email.send_keys('m@mail')
    current_dir = os.path.abspath(os.path.dirname(__file__)) # указываем текущую позицию скрипта
    file_name = "text.txt"                   #имя файла для загрузки
    file_path = os.path.join(current_dir, file_name)     # собираем путь к файлу
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")   # находим кнопку выбора файлов для загрузки
    element.send_keys(file_path)  # передаем путь к загружаемому файлу

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    time.sleep(3)

finally:
    browser.quit()