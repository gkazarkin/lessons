import unittest
from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    browser.find_element_by_class_name("btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer").send_keys(y)
    # input2 = browser.find_element_by_id("robotCheckbox").click()
    # browser.execute_script("window.scrollBy(0, 50);")
    # input3 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_class_name("btn.btn-primary").click()
    # assert "Congratulations! You have successfully registered!" == input1
    # find_element_by_css_selector("[for='python']")

finally:
    time.sleep(6)
    browser.quit()
