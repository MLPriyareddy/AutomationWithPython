from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with the Radio Buttons
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)                                                                                      # False

# driver.find_element_by_id("RESULT_RadioButton-7_1").click()                           # selecting Radio Button
select = driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(select)

# Working with Checkboxes
driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_1").click()
driver.find_element_by_id("RESULT_CheckBox-8_4").click()

driver.close()