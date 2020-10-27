from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.maximize_window()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
RightClick = driver.find_element_by_xpath("//*[@id='authentication']/span")

action=ActionChains(driver)
action.context_click(RightClick).perform()