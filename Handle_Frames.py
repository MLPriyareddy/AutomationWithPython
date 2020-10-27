from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(4)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(4)


driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/div[1]/ul/li[5]").click()
time.sleep(4)

driver.close()