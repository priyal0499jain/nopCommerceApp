import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
import random
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("**********Test__003__add_customer")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.Clicklogin()

        self.logger.info("************Login Successful")
        self.logger.info("*******add customer test starts")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomerMenu()
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        customer_menu_item = wait.until(EC.element_to_be_clickable((By.XPATH, self.addcust.link_customer_item_path)))

        try:
            customer_menu_item.click()
        except Exception as e:
            self.driver.execute_script("arguments[0].click();", customer_menu_item)

        time.sleep(5)

        self.addcust.ClickOnAddNew()
        time.sleep(5)

        self.logger.info("**********providing customer info*******************")

        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Priyal")
        self.addcust.setLastName("Jain")
        self.addcust.setDob("4/01/1999")  # Format: D / MM / YYY
        self.addcust.setCompanyName("Nykaa")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.ClickOnsave()

        # Ensure the save button is clickable and scroll into view

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
