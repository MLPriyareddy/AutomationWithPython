from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# To find Number of input boxes present in a web page
Totalinputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(Totalinputboxes))

# How provide value into a Testbox
driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Angel")
driver.find_element(By.NAME,'RESULT_TextField-2').send_keys("Swaroski")
driver.find_element_by_id("RESULT_TextField-3").send_keys("234567890")
driver.find_element_by_name("RESULT_TextField-4").send_keys("Europe")
driver.find_element_by_name("RESULT_TextField-5").send_keys("Berlin")
driver.find_element_by_id("RESULT_TextField-6").send_keys("aloe32@gmail.com")
time.sleep(5)


# How to get the status
FirstName = driver.find_element(By.ID,'RESULT_TextField-1')
print("First Name is displayed or not:", FirstName.is_displayed())

Country = driver.find_element_by_name("RESULT_TextField-4")
print("Country is enabled or not:", Country.is_enabled())
driver.close()
