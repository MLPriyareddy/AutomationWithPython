from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver_win32/chromedriver")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

Performance =driver.find_element_by_id("menu__Performance")
ReviewsSelection = driver.find_element_by_id("menu_performance_ManageReviews")
ManageReview = driver.find_element_by_id("menu_performance_searchPerformancReview")

actions = ActionChains(driver)
actions.move_to_element(Performance).move_to_element(ReviewsSelection).move_to_element(ManageReview).click().perform()

time.sleep(5)
driver.close()