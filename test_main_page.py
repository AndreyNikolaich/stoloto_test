import time
#from .pages.main_page import LotteryLink
from .pages.main_page import AuthPage
import pytest


@pytest.mark.auth_user
class TestAuthUser (AuthPage):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://www.stoloto.ru/"
        page = AuthPage(browser, link)
        page.open()
        page.login()
        page.should_login()

    def test_go_to_wallet(self, browser):
        link = "https://www.stoloto.ru/"
        page = AuthPage(browser, link)
        page.open()
        page.go_to_wallet()
        page.should_wallet()

    def test_link_7x49_and_by_ticket(self, browser):
        link = "https://www.stoloto.ru/"
        page = AuthPage(browser, link)
        page.open()
        page.go_page_lottery_7x49()
        page.fill_ticket()
        page.should_button_pay()
        page.combination_ticket_in_page()
        page.go_to_pay()
        time.sleep(5)
        page.go_to_tickets_page()



