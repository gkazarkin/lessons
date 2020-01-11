import unittest
from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(6)
    browser.quit()
