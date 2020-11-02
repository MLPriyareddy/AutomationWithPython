import unittest
from selenium import webdriver
import time
import HtmlTestRunner
import sys
sys.path.append("C:/SeleniumProjects/PageObjectModel")
from PageObject.LoginPage import Loginpage


class LoginTest(unittest.TestCase):
    BaseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    UserName = "admin@yourstore.com"
    Password = "admin"
    driver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver_win32/chromedriver")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.BaseURL)
        cls.driver.maximize_window()

    def test_Login(self):
        action = Loginpage(self.driver)
        action.setUsername(self.UserName)
        action.setPassword(self.Password)
        action.ClickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage titles are not same")
        action.ClickLogout()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/SeleniumProjects/PageObjectModel/Report'))