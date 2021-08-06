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
        wd.find_element(*BetOneClick.BUTTON_PAY_ONE_CLICK).click()
        wd.find_element(*BetOneClick.BY_WITHOUT_REGISTRATION).click()
        url_by_without_registration = self.get_current_url()
        assert url_by_without_registration == "https://www.stoloto.ru/guest/payment/login?targetUrl=/payment/bets/service"








