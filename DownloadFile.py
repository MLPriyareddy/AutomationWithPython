from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

ChromeOptions = Options()
ChromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\ScreenShots"})
driver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32\chromedriver", options=ChromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("Download Text document")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
time.sleep(10)

driver.find_element_by_id("pdfbox").send_keys("Download Pdf document")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(10)
driver.close()