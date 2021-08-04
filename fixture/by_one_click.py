from fixture.locators import BetOneClick

class ByOneClickHelper:

    def __init__(self, app):
        self.app = app

    def choise_ticket(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*BetOneClick.TICKET).click()


