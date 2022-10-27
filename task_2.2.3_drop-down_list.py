# Drop-down List

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
num1_element = browser.find_element(By.ID, 'num1')
num1 = num1_element.text
num2_element = browser.find_element(By.ID, 'num2')
num2 = num2_element.text
dropdown_list = Select(browser.find_element(By.ID, 'dropdown'))
dropdown_list.select_by_value(str(int(num1) + int(num2)))
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(10)
browser.quit()
