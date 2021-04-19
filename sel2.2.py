from selenium.webdriver.support.ui import Select
from selenium import webdriver
link="http://suninjuly.github.io/selects1.html"

browser=webdriver.Chrome()
browser.get(link)

value1=browser.find_element_by_id("num1")
x=value1.text
value2=browser.find_element_by_id("num2")
y=value2.text
xy=int(x)+int(y)
xy=str(xy)
select=Select(browser.find_element_by_tag_name("select"))
select.select_by_value((xy))

option1=browser.find_element_by_class_name("btn.btn-default")
option1.click()

