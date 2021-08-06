from fixture.locators import WalletLocators
from fixture.locators import PageLotteryLocators7x49
from fixture.locators import MainPageLocators

class ByTicketHelper:
    def __init__(self, app):
        self.app = app

    def go_to_wallet(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*WalletLocators.WALLET_LINK).click()
        wallet_sum = wd.find_element(*WalletLocators.WALLET_SUM).text
        assert wallet_sum >= '0'

    def fill_ticket_lottery_7x49(self):
        wd = self.app.wd
        wd.find_element(*PageLotteryLocators7x49.LINK_LOTTERY).click()
        wd.find_element(*PageLotteryLocators7x49.AUTO_FILL).click()

    def go_to_pay(self):
        wd = self.app.wd
        if wd.find_element(*WalletLocators.WALLET_SUM).text >= "50":
            wd.find_element(*PageLotteryLocators7x49.BUTTON_PAY).click()
        else:
            print('нехватка средств')
            return False




    def combination_ticket_in_page(self):
        browser = self.browser
        number_page = []
        for element in browser.find_element(*NumbersLottery.NUMBER_PAGE):
            text = int(element.text)
            number_page.append('%02d' % text)
        return number_page

    def combination_tickets_in_page_my_tickets(self):
        element = self.browser.find_element(*NumbersLottery.NUMBER_TICKETS)
        number_ticket = int(element.text)
        return number_ticket

    def go_to_tickets_page(self):
        tickets_page = self.browser.find_element(*MainPageLocators.MY_TICKETS_LINK)
        all_tickets.click()
