import XLUtilis
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.get("https://intellipaat.com/")

driver.maximize_window()

path = "C:/Openpyxl/DataDriven.xlsx"


rows = XLUtilis.getrowcount(path, 'Sheet1')

for r in range(2, rows+1):
    Username = XLUtilis.readdata(path, 'Sheet1', r, 1)
    Password = XLUtilis.readdata(path, 'Sheet1', r, 2)

    driver.find_element_by_xpath("//*[@id='menu-course-new-top-menu']/span[3]/a").click()
    driver.find_element_by_name("log").send_keys(Username)
    driver.find_element_by_name("pwd").send_keys(Password)
    driver.find_element_by_xpath("//*[@id='lwa_wp-submit']").click()

    if driver.title=="Online Professional Training Courses and Certification - Intellipaat":
        print("Login is successfull")
        XLUtilis.writedata(path, 'Sheet1', r, 3, "Login is successfull")
    else:
        print("Login is Failed")
        XLUtilis.writedata(path, "Sheet1", r, 3, "Login is Failed")

driver.find_element_by_xpath("//*[@id='menu-course-new-top-menu']/span[4]/a/img").click()
driver.find_element_by_id("destroy-sessions").click()

