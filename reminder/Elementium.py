"""
#Elementium
import datetime
from elementium.drivers.se import SeElements
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print("Run Started at :" + str(datetime.datetime.now()))
s = SeElements(webdriver.Chrome(ChromeDriverManager().install()))
s.set_window_size(1900, 1000)

print("Run Ended at :" + str(datetime.datetime.now()))
s.browser.quit()

# Методы
se.find('button', wait=True)

# Find by ID
se.find("#foo")

# Find by class name
se.find(".cssClass")

# Find by name
se.find("[name='password']")

# Find by tag name
se.find("input")

# Find by link text
se.find_link("Click me")

# Find by partial link text
se.find_link("Click", exact=False)

search_field = s.find("[name='q']")
search_field.write("google.com" + Keys.RETURN)
# Находим все подписи к заголовкам с адресами сайтов
urls = s.find("cite")
first_url = urls.get(0)
# Выводим в логи его содержание
print(first_url.text())
assert "google.com" in first_url.text(), "Я искал другой сайт :("
"""