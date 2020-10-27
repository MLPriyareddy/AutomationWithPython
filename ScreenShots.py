from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")
driver.get("https://intellipaat.com/signin/")
driver.maximize_window()

# driver.save_screenshot("C:/ScreenShots/Intellipat.png")
#driver.get_screenshot_as_file("C:/ScreenShots/Intellipat2.png")
driver.get_screenshot_as_png()
time.sleep(3)
driver.close()