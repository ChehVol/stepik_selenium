from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
browser.switch_to.alert.accept()  # переходим на всплывающее окно
x = browser.find_element(By.ID, "input_value").text  # читаем значение х
func = log(abs(12 * sin(int(x))))
browser.find_element(By.ID, "answer").send_keys(str(func))
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
answer = browser.switch_to.alert.text
answer = answer.split(': ')[-1]
print(answer)
browser.quit()


#  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#  button.click()
