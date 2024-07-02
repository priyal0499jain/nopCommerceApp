import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from TestCases.test_add_customer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("**********Test__005__add_customer")
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

        self.logger.info("************searching customer by name***************")
        searchcustname = SearchCustomer(self.driver)
        searchcustname.setFirstname("Virat")
        searchcustname.setLastname("Kohli")
        searchcustname.clickSearch()
        time.sleep(5)
        status = searchcustname.SearchCustomerByName("Virat Kohli")
        assert True == status
        self.logger.info("*****************search customer by name process ends******")
