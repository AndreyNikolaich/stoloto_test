from .base_page import BasePage
from .locators import BetOneClick
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class QickPickNoAuth(BasePage):
    def scroll_tickets(self):
        tickets_banner = self.browser.find_element(*BetOneClick.BET_ONE_CLICK)
        #tickets_banner.is_element_present()
        tickets_banner.visible_css('[class="bet1click_card bg_keno show6"]', t=30)

    def choice_ticket(self):
        ticket = self.browser.find_element(*BetOneClick.TICKET)

        ticket.click()



