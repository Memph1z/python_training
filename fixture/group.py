class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("new").click()
        self.fill_group_info(group)
        driver.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_info(self, group):
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        self.fill_group_info(group)
        driver.find_element_by_name("update").click()
        self.return_to_group_page()