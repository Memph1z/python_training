from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver_path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        # self.driver.implicitly_wait(2)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            # noinspection PyStatementEffect
            self.driver.current_url
            return True
        except:
            return False

    def go_to_home_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home page").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook")

    def destroy(self):
        self.driver.quit()