from selenium import webdriver
import time
import math

link="http://suninjuly.github.io/redirect_accept.html"
browser=webdriver.Chrome()
browser.get(link)

option1=browser.find_element_by_class_name("trollface.btn.btn-primary")
option1.click()

new_window=browser.window_handles[1]
browser.switch_to.window(new_window)

option2=browser.find_element_by_id("input_value")
x=option2.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

xy=calc(x)

option3=browser.find_element_by_name("text")
option3.send_keys(xy)

option4=browser.find_element_by_class_name("btn.btn-primary")
option4.click()