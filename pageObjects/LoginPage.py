from selenium.webdriver.common.by import By


class LoginPage:
    text_username_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    login_button_xpath = "//button[normalize-space()='Log in']"
    logout_button_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def Clicklogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def Clicklogout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
