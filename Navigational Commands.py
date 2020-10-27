from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://intellipaat.com/signup/")
print(driver.title)
time.sleep(3)

driver.get("https://intellipaat.com/corporate-training/")
print(driver.title)
time.sleep(2)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)
driver.close()