from fixture.locators import MainPageLocators


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*MainPageLocators.LOGIN_LINK).click()
        wd.find_element(*MainPageLocators.LOGIN_EMAIL).send_keys(str('9998082383'))
        wd.find_element(*MainPageLocators.LOGIN_PASSWORD).send_keys(str('Test2021'))
        wd.find_element(*MainPageLocators.LOGIN_IN).click()
        user_name = wd.find_element(*MainPageLocators.USER_NAME).text
        assert user_name == "Andrey"

    def logout(self):
        wd = self.app.wd
        wd.find_element(*MainPageLocators.LOGOUT).click()
