from fixture.locators import MainPageLocators
from fixture.locators import WalletLocators
from fixture.locators import PageLotteryLocators7x49
from .base_page import BasePage
from fixture.locators import NumbersLottery
from selenium.webdriver.common.by import By

class AuthPage(BasePage):
    #def open_page(self):
        #link = "https://www.stoloto.ru/"
        #link.click()

    def login(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        enter_email = self.browser.find_element(*MainPageLocators.LOGIN_EMAIL)
        enter_email.send_keys(str('9998082383'))
        enter_password = self.browser.find_element(*MainPageLocators.LOGIN_PASSWORD)
        enter_password.send_keys(str('Test2021'))
        login = self.browser.find_element(*MainPageLocators.LOGIN_IN)
        login.click()

    def should_login(self):
        user_name = self.browser.find_element(*MainPageLocators.USER_NAME).text
        assert user_name == "Andrey"

    def go_to_wallet(self):
        wallet_link = self.browser.find_element(*WalletLocators.WALLET_LINK)
        wallet_link.click()

    def should_wallet(self):
        wallet_sum = self.browser.find_element(*WalletLocators.WALLET_SUM).text
        assert wallet_sum >= '0'

    def go_page_lottery_7x49(self):
        page_lottery = self.browser.find_element(*PageLotteryLocators7x49.LINK_LOTTERY)
        page_lottery.click()

    def fill_ticket(self):
        auto_fill = self.browser.find_element(*PageLotteryLocators7x49.AUTO_FILL)
        auto_fill.click()

    def go_to_pay(self):
        if self.browser.find_element(*WalletLocators.WALLET_SUM) >= "25":
            button_pay_wallet = self.browser.find_element(*PageLotteryLocators7x49.BUTTON_PAY)
            button_pay_wallet.click()
        else:
            print('нехватка средств')
            return None


    def should_button_pay(self):
        assert self.is_element_present(By.XPATH,'//*[@id="content"]/div[5]/div/div/div[2]/div[4]/form[5]/input[2]'), "element is not present"


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
        tickets_page.click()
        all_tickets = self.browser.find_element(*MainPageLocators.ALL_TICKETS)
        all_tickets.click()
