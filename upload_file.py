import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys('Vitaliy')
browser.find_element(By.CSS_SELECTOR, '[name=lastname]').send_keys('Dubinin')
browser.find_element(By.CSS_SELECTOR, '[name=email]').send_keys('vit.du@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

#button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()