import time

class InterestingHelper:

    def __init__(self, app):
        self.app = app

    def get_current_url(self):
        wd = self.app.wd
        time.sleep(1)
        return str(wd.current_url)

    def interesting_lotteries(self):
        wd = self.app.wd
        time.sleep(4)
        home_page = wd.window_handles
        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_ZL_statistics"]').click() #ЖЛ
        time.sleep(2)
        zh_l_page = wd.window_handles
        wd.switch_to.window(zh_l_page[1])
        zh_l_url = self.get_current_url()
        assert zh_l_url == "https://media.stoloto.ru/article/zhilischnaya-lotereya-v-cifrah"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_won_2times"]').click() #Любимцы
        time.sleep(2)
        favorite_page = wd.window_handles
        wd.switch_to.window(favorite_page[2])
        favorite_url = self.get_current_url()
        assert favorite_url == "https://media.stoloto.ru/article/vezunchiki-po-zhizni-vyigrali-v-lotereyu-dvazhdy"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_znaniye_loterey"]').click() #Тест знание лотерей
        time.sleep(2)
        test_page = wd.window_handles
        wd.switch_to.window(test_page[3])
        test_url = self.get_current_url()
        assert test_url == "https://media.stoloto.ru/quiz/naskolko-horosho-vy-razbiraetes-v-lotereyah"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_museum"]').click() #музей
        time.sleep(4)
        museum_page = wd.window_handles
        wd.switch_to.window(museum_page[4])
        museum_url = self.get_current_url()
        assert museum_url == "https://museum.stoloto.ru/"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_play_online"]').click() #играй онлайн
        time.sleep(2)
        play_page = wd.window_handles
        wd.switch_to.window(play_page[5])
        play_url = self.get_current_url()
        assert play_url == "https://www.stoloto.ru/safety"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_scammers"]').click() #мошенники
        time.sleep(2)
        scammers_page = wd.window_handles
        wd.switch_to.window(scammers_page[6])
        scammers_url = self.get_current_url()
        assert scammers_url == "https://www.stoloto.ru/warning-lottery-scam/"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_all_lotteries"]').click() #все о лотереях
        time.sleep(2)
        all_lottery_page = wd.window_handles
        wd.switch_to.window(all_lottery_page[7])
        all_lottery_url = self.get_current_url()
        assert all_lottery_url == "https://www.stoloto.ru/state-lottery"
        wd.switch_to.window(home_page[0])
        time.sleep(1)

        wd.find_element_by_css_selector('[data-banner-name="interesting_lottery_telegram_channel"]').click() #TG
        time.sleep(2)
        tg_page = wd.window_handles
        wd.switch_to.window(tg_page[8])
        tg_url = self.get_current_url()
        assert tg_url == "https://t.me/aboutstoloto"
        wd.switch_to.window(home_page[0])
        time.sleep(1)
        pass