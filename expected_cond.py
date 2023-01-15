from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from math import log, sin

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

message = WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element(By.ID, "book")
button.click()

x = browser.find_element(By.ID, "input_value").text  # читаем значение х
func = log(abs(12 * sin(int(x))))
answer = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)  # Пролистываем страницу
answer.send_keys(str(func))
browser.find_element(By.ID, "solve").click()

code = browser.switch_to.alert.text   # читаем ответ из alert
code = code.split(': ')[-1]
print(code)

browser.quit()
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
