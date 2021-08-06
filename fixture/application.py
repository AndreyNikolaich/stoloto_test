from selenium import webdriver
from fixture.session import SessionHelper
from fixture.by_one_click import ByOneClickHelper
from fixture.social_links import SocialLinksHelper

class Application:

    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.by_one_click = ByOneClickHelper(self)
        self.social_links = SocialLinksHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get("https://www.stoloto.ru/")
        wd.maximize_window()


    def destroy(self):
        self.wd.quit()


