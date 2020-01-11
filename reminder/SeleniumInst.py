"""
# Установка
pip install selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5) # Неявное ожидание
link = "http://suninjuly.github.io/wait1.html"
browser.get(link)

или
driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds

"""