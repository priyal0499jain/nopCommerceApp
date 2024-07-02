import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from TestCases.test_add_customer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("**********Test__003__add_customer")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.Clicklogin()
        time.sleep(5)

        self.logger.info("************Login Successful*************")
        self.logger.info("************search customer process starts***********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomerMenu()
        self.addcust.ClickOnCustomerMenuItem()

        self.logger.info("************searching customer by emailid***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.SearchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*****************search customer by email process ends******")
