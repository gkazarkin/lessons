"""
#Selenium
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")

from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')

driver.find_element_by_id('loginForm')
find_element_by_name('username')
find_element_by_xpath("//input[@name='continue'][@type='button']")
find_element_by_link_text('Continue')
find_element_by_partial_link_text('Cont')
find_element_by_tag_name('h1') или ("input")
find_element_by_class_name('content')
find_element_by_class_name("btn.btn-default")
find_element_by_css_selector('p.content')
find_element_by_css_selector("[for='python']")

find_elements_by_name и т.д.

"""