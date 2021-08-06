from fixture.locators import BetOneClick
import time

class ByOneClickHelper:

    def __init__(self, app):
        self.app = app

    def get_current_url(self):
        wd = self.app.wd
        time.sleep(1)
        return str(wd.current_url)

    def choice_ticket(self):
        wd = self.app.wd
        self.app.open_home_page()
        game_name = wd.find_element(*BetOneClick.TICKET).get_attribute(str("href"))
        wd.find_element(*BetOneClick.TICKET).click()
        url = self.get_current_url()
        if not url == game_name:
            return False






