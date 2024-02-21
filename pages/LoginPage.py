from pages.BasePage import BasePage
from appium.webdriver.common.mobileby import By



class LoginPage(BasePage):

    username_input = (By.CLASS_NAME, "XCUIElementTypeTextField")
    password_input = (By.CLASS_NAME, "XCUIElementTypeSecureTextField")
    login_btn = (By.XPATH, '//XCUIElementTypeButton[@name="Sign in"]')
    auto_login_memory_checkbox = (By.CLASS_NAME, "XCUIElementTypeImage")
    policy_checkbox = (By.NAME, 'rgt disagree')
    endUser_btn = (By.NAME, "ZDLogUN")
    engineer_btn = (By.NAME, "YWLogUN")


    def click_login_btn(self):
        self.find_element(*self.username_input).click()

    def engineer_login(self, username, password):
        self.driver.find_element(*self.engineer_btn).click()
        area_username = self.driver.find_element(By.CLASS_NAME, "XCUIElementTypeTextField")
        area_username.clear()
        area_username.send_keys(username)
        self.find_element(*self.password_input).send_keys(password)
        self.find_element(*self.login_btn).click()
