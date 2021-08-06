from selenium import webdriver
from fixture.session import SessionHelper
from fixture.by_one_click import ByOneClickHelper
from fixture.social_links import SocialLinksHelper
from fixture.by_ticket import ByTicketHelper


class Application:

    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.by_one_click = ByOneClickHelper(self)
        self.social_links = SocialLinksHelper(self)
        self.base_url = base_url
        self.by_ticket = ByTicketHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        current_url = self.social_links.get_current_url()
        if not self.base_url == current_url:
            wd.get(self.base_url)
            wd.maximize_window()


    def destroy(self):
        self.wd.quit()


