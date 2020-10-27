from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.maximize_window()

driver.get("https://intellipaat.com/signin/")

driver.implicitly_wait(12)

assert "Signin - Intellipaat" in driver.title

driver.find_element(By.NAME, "log").send_keys("priyakarumuri16")
driver.find_element(By.NAME, 'pwd').send_keys("Karumuri@2020")
driver.find_element(By.ID, "lwa_wp-submit").click()

driver.close()

