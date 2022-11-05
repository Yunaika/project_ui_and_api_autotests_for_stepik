from selene import be
from selene.support.shared import browser


def click_close_button():
    if browser.element('.mobile-banner__close-button').matching(be.visible):
        browser.element('.mobile-banner__close-button').click()
