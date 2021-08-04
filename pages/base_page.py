from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pytest

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def visible_xpath(self, element, t):
        wd = self.browser
        for i in range(t):
            try:
                if wd.find_element_by_xpath(element).is_displayed():
                    break
            except:
                pass
            time.sleep(1)
        else:
            print('нет элемента')
            #pytest.fail("Не найден элемент " + element)

    def visible_css(self, element, t):
        wd = self.browser
        for i in range(t):
            try:
                if wd.find_element_by_css_selector(element).is_displayed():
                    break
            except:
                pass
            time.sleep(1)
        else:
            print("Элемент не найден")
            #self.app.screenshot.maker()
            #pytest.fail("Не найден элемент " + element)