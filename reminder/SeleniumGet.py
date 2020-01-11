"""
# Берёт текст или атрибут
x = browser.find_element_by_id("input_value").text = Берёт текст между открывающим и закрывающим тегами
checked = browser.find_element_by_id("peopleRule").get_attribute("checked") = берёт атрибут checked (radiobutton)
assert checked is not None, "People radio is not selected by default"
assert checked == "true", "People radio is not selected by default"
Аналогично можно проверить "disabled"

# Парскинг строк
Метод split возвращает список, в качестве разделителя используем 'двоеточие пробел',  берём последний элемент, это нужное нам число.
alert_number = alert_text.split(': ')[-1]

import pyperclip
import split
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
s.find(email).write(paste)

# CTRL + C, CTRL + V
import pyperclip
paste = pyperclip.paste()
или paste2 = Keys.CONTROL + Keys.INSERT
print("paste is: " + paste)
s.find(email).write(paste)
# Но в контейнере нет буфера, так что лучше сразу в переменную
# На ubuntu
sudo apt-get install xsel
или
sudo apt-get install xclip

# Ждать загрузку страницы
driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);

# Cookies
# Перейти на необходимый домен
driver.get("http://www.example.com")
# Установить куки. Следующий cookie действителен для всего домена
cookie = {"ключ": "значение"}
driver.add_cookie(cookie)
# И теперь получим все доступные куки для текущего адреса URL
all_cookies = driver.get_cookies()
for cookie_name, cookie_value in all_cookies.items():
    print("%s -> %s", cookie_name, cookie_value)

"""