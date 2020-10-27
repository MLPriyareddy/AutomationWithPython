from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element = driver.find_element_by_name("RESULT_RadioButton-9")
drop = Select(element)

# How to count Number of options in webpage
print(len(drop.options))

# Copy all the options and print them on console
all_options = drop.options
for option in all_options:
    print(option.text)


# Selecting by visible Text
#drop.select_by_visible_text("Morning")              # Morning

# Selecting by Index
drop.select_by_index(2)                             # Afternoon

# select by value
#drop.select_by_value("Radio-2")                     # Evening
time.sleep(5)
driver.close()