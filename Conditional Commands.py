from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://intellipaat.com/signup/")
time.sleep(5)
FirstName = driver.find_element_by_name("sr_firstname")
print(FirstName.is_displayed())
print(FirstName.is_enabled())

LastName = driver.find_element_by_id("reg_sr_lastname")
print(LastName.is_displayed())
print(LastName.is_enabled())

FirstName.send_keys("Priya")
LastName.send_keys("Karumuri")
time.sleep(10)
driver.close()
