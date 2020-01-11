import unittest
from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    input1 = browser.find_element_by_name("firstname").send_keys("fafafa")
    input2 = browser.find_element_by_name("lastname").send_keys("fafafa")
    input3 = browser.find_element_by_name("email").send_keys("fafafa@affaf.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(os.path.abspath(os.path.dirname(__file__)))
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    input4 = browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    time.sleep(5)
    browser.quit()
