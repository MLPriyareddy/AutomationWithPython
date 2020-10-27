from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://intellipaat.com/signup/")
time.sleep(3)
print(driver.title)
print(driver.current_url)
driver.close()