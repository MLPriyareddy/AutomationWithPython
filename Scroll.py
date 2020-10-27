from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# Scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)", " ")

# Scroll down a Webpage based on element
CountryFlag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[63]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", CountryFlag)

# scroll down the webpage till end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(5)
driver.close()