import time
from fixture.locators import FooterLoc
from selenium.webdriver.common.action_chains import ActionChains

class InviteFriendHelper:

    def __init__(self, app):
        self.app = app

    def get_current_url(self):
        wd = self.app.wd
        time.sleep(1)
        return str(wd.current_url)

    def open_invite_page(self):
        wd = self.app.wd
        invite_page_link = wd.find_element(*FooterLoc.INVITE_FRIENDS).get_attribute(str("href"))
        wd.find_element(*FooterLoc.INVITE_FRIENDS).click()
        time.sleep(5)
        invite_page = self.get_current_url()
        assert invite_page == invite_page_link

    def invite_slider(self):
        wd = self.app.wd
        slider_one = wd.find_element_by_css_selector('.ui-slider-pip-first> .ui-slider-line')
        ActionChains(wd).click(slider_one).perform()
        time.sleep(2)
        special_bonus = wd.find_element_by_css_selector('[class="special-bonus"] ins').text
        bonus = wd.find_element_by_css_selector('[class="bonus"] ins').text
        if special_bonus == "1" and bonus == "9":
            return True
        else:
            print('не верное значение бонусов / спецбонусов')
            return False

