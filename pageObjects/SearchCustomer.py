from selenium.webdriver.common.by import By


class SearchCustomer:
    text_box_email_xpath = "//input[@id='SearchEmail']"
    text_box_first_name_xpath = "//input[@id='SearchFirstName']"
    text_box_last_name_xpath = "//input[@id='SearchLastName']"
    btn_search_xpath = "//button[@id='search-customers']"

    table_search_results_xpath = "//div[@class='dataTables_scrollBody']"
    table_xpath = "//table[@id ='customers-grid']"
    table_rows_xpath = "//div[@class='card card-default']//div[@class='card-body']"
    table_column_xpath = "//table[@id ='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_box_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_email_xpath).send_keys(email)

    def setFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.text_box_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_first_name_xpath).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.XPATH, self.text_box_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_last_name_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def SearchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id ='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                return True
            else:
                return False

    def SearchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id ='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                return True
            else:
                return False
