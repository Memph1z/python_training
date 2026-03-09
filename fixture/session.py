

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len (driver.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, login, password):
        if self.is_logged_in():
            if self.is_logged_in_as(login):
                return
            else:
                self.logout()
        self.login(login, password)

    def is_logged_in_as(self, login):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div/div[1]/form/b").text == "("+login+")"

