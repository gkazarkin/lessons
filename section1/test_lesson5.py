import unittest
from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
link = "http://suninjuly.github.io/registration2.html"

try:
    #Используется драйвер менеджер, который испортируется выше
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    # input1 = browser.find_element_by_tag_name("input")
    input1 = browser.find_element_by_class_name("form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2 = browser.find_element_by_class_name("form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("Smolensk@1.ru")
    # input4 = browser.find_element_by_xpath("//div/form/div[2]/div[1]/input")
    # input4.send_keys("895392348121")
    # input5 = browser.find_element_by_xpath("//div/form/div[2]/div[2]/input")
    # input5.send_keys("tomsk 21")
    # button = browser.find_element_by_xpath("//div[6]/button[3]")
    # button.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

    # elements = browser.find_elements_by_tag_name("input")
    # for element in elements:
    #    element.send_keys("Мой ответ")

    # button = browser.find_element_by_css_selector("btn-default")
    # button.click()

finally:
    time.sleep(5)
    browser.quit()

# math_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
# print(math_link)

# chromedriver = 'C:\Users\Ark\PycharmProjects\chromedriver\chromedriver.exe'