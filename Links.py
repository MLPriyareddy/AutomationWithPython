from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")
driver.maximize_window()
driver.get("https://www.starbucks.com/account/signin")

# To check Number of links
links = driver.find_elements(By.TAG_NAME, 'a')
print("Number of links present in Starbucks:", len(links))

# Print links
for starbucks in links:
    print(starbucks.text)
# Click on Particular Link using Link or Partial Link Text
driver.find_element_by_link_text("Forgot your password?").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Find").click()
driver.close()