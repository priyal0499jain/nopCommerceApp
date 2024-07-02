import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******************TestLogin_1*************")
        self.logger.info("******************Verifying Home Page Title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************Test Case Passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_login.png")
            self.driver.close()
            self.logger.error("******************Test Case Failed*************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************Verifying Login Test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.Clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******************Login Test Case Passed*************")
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("******************Login Test Case Failed*************")
            assert False
