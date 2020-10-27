from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

# Accept alert
a=driver.switch_to.alert
a.accept()
time.sleep(2)

# dismiss alert
b = driver.switch_to.alert
b.dismiss()

time.sleep(2)
driver.close()