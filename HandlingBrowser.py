from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

handles = driver.window_handles
for h in handles:
    driver.switch_to.window(h)
    print(driver.title)
    if driver.title == "SeleniumHQ Browser Automation":               # To close specific window
        driver.close()


# driver.quit()            # Close all windows
# driver.close             # close Parent window
