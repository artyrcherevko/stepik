from selenium import webdriver
import os

link="http://suninjuly.github.io/file_input.html"
browser=webdriver.Chrome()
browser.get(link)

option1=browser.find_element_by_name("firstname")
option1.send_keys("AA")
option2=browser.find_element_by_name("lastname")
option2.send_keys("BB")
option3=browser.find_element_by_name("email")
option3.send_keys("CC")

current_dir=os.path.abspath(os.path.dirname(__file__))
file_path=os.path.join(current_dir,"text.txt")

option4=browser.find_element_by_name("file")
option4.send_keys(file_path)

bt=browser.find_element_by_class_name("btn.btn-primary")
bt.click()