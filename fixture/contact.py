from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_xpath("//input[19]").click()
        self.app.go_to_home_page()

    def delete_first_contact(self):
        driver = self.app.driver
        self.open_home_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.app.go_to_home_page()

    def edit_first_contact(self, contact):
        driver = self.app.driver
        self.open_home_page()
        driver.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        driver.find_element_by_name("update").click()
        self.app.go_to_home_page()

    def open_home_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/index.php") and len (driver.find_elements_by_name("delete")) > 0):
            driver.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.select_value("bday", contact.bday)
        self.select_value("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)
        self.select_value("aday", contact.aday)
        self.select_value("amonth", contact.amonth)
        self.change_field("ayear", contact.ayear)

    def select_value(self, field_name, value):
        driver = self.app.driver
        if value is not None:
            driver.find_element_by_name(field_name).click()
            Select(driver.find_element_by_name(field_name)).select_by_visible_text(value)

    def change_field(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def count(self):
        driver = self.app.driver
        self.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        driver = self.app.driver
        self.open_home_page()
        contacts = []
        for element in driver.find_elements_by_xpath("//tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            contact_id_value = cells[0].find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(contact_id=contact_id_value, lastname=lastname, firstname=firstname))
        return contacts