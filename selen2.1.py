from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

klad=browser.find_element_by_id("treasure")
klad1 = klad.get_attribute("valuex")
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x=klad1
y=calc(x)

option1=browser.find_element_by_id("answer")
option1.send_keys(y)
option2=browser.find_element_by_id("robotCheckbox")
option2.click()
option3=browser.find_element_by_id("robotsRule")
option3.click()
option4=browser.find_element_by_class_name("btn.btn-default")
option4.click()