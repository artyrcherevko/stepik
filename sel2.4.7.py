from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
link="http://suninjuly.github.io/explicit_wait2.html"
browser=webdriver.Chrome()
browser.get(link)

option1=WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
option2=browser.find_element_by_id("book")
option2.click()


option3=browser.find_element_by_id("input_value")
x=option3.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

xy=calc(x)
option4=browser.find_element_by_id("answer")
option4.send_keys(xy)
option5=browser.find_element_by_class_name("btn.btn-primary")
option5.click()
