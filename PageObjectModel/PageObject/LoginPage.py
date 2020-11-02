class Loginpage():
    textbox_Username_byID = "Email"
    textbox_Password_byID = "Password"
    button_Login_byXpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    link_Logout_bylink_Text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,Username):
        self.driver.find_element_by_id(self.textbox_Username_byID).clear()
        self.driver.find_element_by_id(self.textbox_Username_byID).send_keys(Username)

    def  setPassword(self, Password):
        self.driver.find_element_by_id(self.textbox_Password_byID).clear()
        self.driver.find_element_by_id(self.textbox_Password_byID).send_keys(Password)

    def ClickLogin(self,):
        self.driver.find_element_by_xpath(self.button_Login_byXpath).click()

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.link_Logout_bylink_Text).click()