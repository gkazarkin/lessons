import unittest
from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    x = int(x)
    y = int(y)
    print(x, y)

    z = x + y
    print(z)
    w = str(z)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(w)
    input1 = browser.find_element_by_class_name("btn.btn-default").click()

    # browser.execute_script("alert('Robots at work');")

    # assert "Congratulations! You have successfully registered!" == input1
    # find_element_by_css_selector("[for='python']")

finally:
    time.sleep(5)
    browser.quit()
