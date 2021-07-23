from .pages.social_links import SocialLinksBase


def test_social_links(browser):
    link = "https://www.stoloto.ru/"
    page = SocialLinksBase(browser, link)
    page.open()
    page.social_links()
