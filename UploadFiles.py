from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()


driver.switch_to.frame(0)
driver.find_element_by_name("RESULT_FileUpload-10").send_keys("C://Openpyxl//Fruits//Fruits")

time.sleep(5)
driver.close()