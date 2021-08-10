from fixture.locators import MainPageLocators


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("div.logout a.with_extra_active_area")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.name a").text

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*MainPageLocators.LOGIN_LINK).click()
        wd.find_element(*MainPageLocators.LOGIN_EMAIL).send_keys(username)
        wd.find_element(*MainPageLocators.LOGIN_PASSWORD).send_keys(password)
        wd.find_element(*MainPageLocators.LOGIN_IN).click()
        user_name = wd.find_element(*MainPageLocators.USER_NAME).text
        assert user_name == "Andrey"

    def logout(self):
        wd = self.app.wd
        wd.find_element(*MainPageLocators.LOGOUT).click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()