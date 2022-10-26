# Checkboxes and Radiobuttons

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
text_field = browser.find_element(By.ID, 'answer')
text_field.send_keys(y)
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(10)
browser.quit()
