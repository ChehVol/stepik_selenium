from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

browser = webdriver.Chrome()


def registration(link):
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("Voland")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Chehov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("@mail")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


def test_reg1():
    registration("http://suninjuly.github.io/registration1.html")
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", 'Registratoin1 is failed'


def test_reg2():
    registration("http://suninjuly.github.io/registration2.html")
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", 'Registratoin2 is failed'


if __name__ == "__main__":
    pytest.main()
