from selene.support.shared import browser

from autotest_stepik_project.utils.patching.allure.report import step


class HeaderMenu:
    def __init__(self):
        self.drop_down_profile_menu = DropDownProfileMenu()

    def click_on_logo(self):
        browser.element('.navbar__logo-link').with_(timeout=10).click()
        return self

    def click_on_menu_item_catalog(self):
        browser.element('[data-navbar-item="catalog"]').click()
        return self

    def click_on_menu_item_learn(self):
        browser.element('[data-navbar-item="learn"]').click()
        return self

    def click_on_menu_item_teach(self):
        browser.element('[data-navbar-item="teach"]').click()
        return self

    @step
    def click_on_profile_icon(self):
        browser.element('.navbar__profile-toggler').with_(timeout=10).click()
        return self


class DropDownProfileMenu:
    def click_on_profile(self):
        browser.element('[data-qa="menu-item-profile"]').click()
        return self

    def click_on_settings(self):
        browser.element('[data-qa="menu-item-settings"]').click()
        return self

    def click_on_notifications(self):
        browser.element('[data-qa="menu-item-notifications"]').click()
        return self

    @step
    def click_on_news(self):
        browser.element('[data-qa="menu-item-news"]').click()
        return self

    def click_on_logout(self):
        browser.element('[data-qa="menu-item-logout"]').click()
        return self


