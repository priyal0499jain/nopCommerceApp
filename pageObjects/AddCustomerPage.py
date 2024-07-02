import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    link_customer_menu_path = "(//p[contains(text(),'Customers')])[1]"
    link_customer_item_path = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_path = "//a[normalize-space()='Add new']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_pass_xpath = "//input[@id='Password']"
    textbox_firstname_xpath = "//input[@id='FirstName']"
    textbox_lastname_xpath = "//input[@id='LastName']"
    rd_btn_gender_male = "//input[@id='Gender_Male']"
    rd_btn_gender_female = "//input[@id='Gender_Female']"
    txt_box_dob = "//input[@id='DateOfBirth']"
    txt_box_companyname = "//input[@id='Company']"
    txt_box_customerroles_xpath = "(//span[@role='combobox'])[2]"
    lst_item_vendor_xpath = "//select[@id='VendorId']"
    lst_item_administrator_path = "//*[@id='select2-SelectedCustomerRoleIds-result-r8jq-1']"
    lst_item_forum_path = "//*[@id='select2-SelectedCustomerRoleIds-result-gj4y-2']"
    lst_item_registered_path = "//*[@id='select2-SelectedCustomerRoleIds-result-qdoq-3']"
    lst_item_guests_path = "/html/body/span/span/span/ul/li[4]"
    lst_item_vendors_path = "//*[@id='select2-SelectedCustomerRoleIds-result-llut-5']"
    drp_down_manager_vendor_xpath = "(//select[@id='VendorId'])[1]"
    txt_area_admin_comment = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_path).click()

    def ClickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_customer_item_path).click()

    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_path).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_pass_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txt_box_customerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_registered_path)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_administrator_path)
        elif role == 'Guests':
            time.sleep(3)

            self.driver.find_element(By.XPATH, "//span[@role='presentation']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_guests_path)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_registered_path)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_vendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_guests_path)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_down_manager_vendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rd_btn_gender_male).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rd_btn_gender_female).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_btn_gender_female).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txt_box_dob).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_box_companyname).send_keys(companyname)

    def setAdminContent(self, admincontent):
        self.driver.find_element(By.XPATH, self.txt_area_admin_comment).send_keys(admincontent)

    def ClickOnsave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
