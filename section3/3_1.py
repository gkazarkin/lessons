from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(12)
    browser.get(link)

    # price = browser.find_element_by_id("price")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    bookBtn = browser.find_element_by_id("book").click()
    browser.execute_script("window.scrollBy(0, 70);")

    x = browser.find_element_by_id("input_value").text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer").send_keys(y)
    # button = browser.find_element_by_class_name("btn.btn-primary").click()
    button = browser.find_element_by_id("solve").click()
    # 28.96635248688339

finally:
    time.sleep(7)
    browser.quit()
