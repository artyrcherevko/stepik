from selenium import webdriver
import time
import math
link="http://suninjuly.github.io/alert_accept.html"
browser=webdriver.Chrome()
browser.get(link)


option1=browser.find_element_by_class_name("btn.btn-primary")
option1.click()
confirm=browser.switch_to_alert()
confirm.accept()


num1=browser.find_element_by_id("input_value")
x=num1.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y=calc(x)
num2=browser.find_element

option2=browser.find_element_by_id("answer")

option2.send_keys(y)

option3=browser.find_element_by_class_name("btn.btn-primary")
option3.click()