import time

class SocialLinksHelper:

    def __init__(self, app):
        self.app = app

    def get_current_url(self):
        wd = self.app.wd
        time.sleep(1)
        return str(wd.current_url)

    def social_links(self):
        wd = self.app.wd
        time.sleep(4)
        home_page = wd.window_handles
        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li").click()  # vk
        time.sleep(2)
        vk_page = wd.window_handles
        wd.switch_to.window(vk_page[1])
        vk_url = self.get_current_url()
        assert vk_url == "https://vk.com/stoloto"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li[2]").click()  # fb
        time.sleep(2)
        fb_page = wd.window_handles
        wd.switch_to.window(fb_page[2])
        fb_url = self.get_current_url()
        assert fb_url == "https://www.facebook.com/stoloto.ru"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li[3]").click()  # odnoclass
        time.sleep(2)
        ok_page = wd.window_handles
        wd.switch_to.window(ok_page[3])
        ok_url = self.get_current_url()
        assert ok_url == "https://ok.ru/stoloto"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li[4]").click()  # insta
        time.sleep(2)
        inst_page = wd.window_handles
        wd.switch_to.window(inst_page[4])
        inst_url = self.get_current_url()
        assert inst_url == "https://www.instagram.com/stoloto/" or "https://www.instagram.com/accounts/login/"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li[5]").click()  # youtube
        time.sleep(2)
        yt_page = wd.window_handles
        wd.switch_to.window(yt_page[5])
        yt_url = self.get_current_url()
        assert yt_url == "https://www.youtube.com/channel/UCeCL_BTYDdZeL0ZvAUwzK2Q" or "https://www.youtube.com/c/stolototv"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li[6]").click()  # twitter
        time.sleep(2)
        tw_page = wd.window_handles
        wd.switch_to.window(tw_page[6])
        tw_url = self.get_current_url()
        assert tw_url == "https://twitter.com/stoloto"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='navigation']/div/div[5]/div/ul/li[7]").click()  # telegram
        time.sleep(2)
        tg_page = wd.window_handles
        wd.switch_to.window(tg_page[7])
        tg_url = self.get_current_url()
        assert tg_url == "https://t.me/aboutstoloto"
        wd.switch_to.window(home_page[0])
        time.sleep(1)
        pass
