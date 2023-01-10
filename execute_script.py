from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, "input_value").text # читаем значение х
func = log(abs(12 * sin(int(x))))
answer = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer) # Пролистываем страницу
answer.send_keys(str(func))
browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()
browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

#button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()