from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
Doubleclick = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

action = ActionChains(driver)
action.double_click(Doubleclick).perform()
time.sleep(3)
driver.close()