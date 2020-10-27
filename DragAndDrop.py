from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
Rome = driver.find_element_by_id("box6")
italy = driver.find_element_by_xpath("//*[@id='box106']")
seoul = driver.find_element_by_id("box5")
south_korea = driver.find_element_by_xpath("//*[@id='box105']")
oslo = driver.find_element_by_id("box1")
Norway = driver.find_element_by_xpath("//*[@id='box101']")

action=ActionChains(driver)
action.drag_and_drop(Rome, italy).drag_and_drop(seoul, south_korea).drag_and_drop(oslo, Norway).perform()

time.sleep(7)
driver.close()