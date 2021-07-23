from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '[class="iconic iconic-user"]')
    LOGIN_EMAIL = (By.XPATH, '//*[@id="auth_login"]')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="auth_password"]')
    LOGIN_IN = (By.CSS_SELECTOR, '[class="pretty_button_new pretty_button type_primary btn_l scaller"]')
    USER_NAME = (By.XPATH, '//*[@id="layout"]/div[1]/div/div[1]/div[2]/div[1]/div/a')
    MY_TICKETS_LINK = (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/small/p/a')
    ALL_TICKETS = (By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div/ul/li[1]/ul/li[1]/a')

class WalletLocators():
    WALLET_SUM = (By.XPATH, '//*[@id="layout"]/div[6]/div[1]/div/div[1]/div/div[1]/span[2]/span')
    BUTTON_WALLET_REFRESH = (By.XPATH, '//*[@id="layout"]/div[6]/div[1]/div/div[1]/div/div[1]/span[3]')
    WALLET_LINK = (By.XPATH, '//*[@id="layout"]/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/a')

class PageLotteryLocators7x49():
    LINK_LOTTERY = (By.XPATH, '//*[@id="item_5150"]/a')
    AUTO_FILL = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div[1]/div/div/div[7]/div[1]/span[1]')
    BUTTON_PAY = (By.XPATH, '//*[text()="Оплатить из кошелька"]')

class NumbersLottery():
    NUMBER_PAGE = (By.CSS_SELECTOR, "b.game_number.selected")
    NUMBER_TICKETS = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/dl/dd')

class UpsaleBanners():
    BANNER_IN_PAGE_PAY = (By.XPATH, '//*[@id="content"]/div[2]/div')

#class ElementLocators():

