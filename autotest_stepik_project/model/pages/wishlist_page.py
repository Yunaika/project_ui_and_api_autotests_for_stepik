from selene import have, be
from selene.support.shared import browser


class Item:
    def __init__(self):
        self.dropdown_menu = DropDownMenu()

    def click_menu_item_icon(self, value):
        browser.element('.item-tile-list').all('.item-tile') \
            .element_by_its('.item-tile__title-link', have.exact_text(str(value))) \
            .element('.item-tile__tools').element('.item-tile__menu').click()
        return self

    def should_have_title(self, value):
        browser.element('.item-tile-list').all('.item-tile') \
            .element_by_its('.item-tile__title', have.exact_text(value)).should(be.visible)
        return self


class DropDownMenu:
    drop_down_menu = browser.element('.drop-down__body')

    def click_buy(self):
        self.drop_down_menu.element('.menu-item-enroll').click()
        return self

    def click_join_course(self):
        self.drop_down_menu.element('.menu-item-enroll').click()
        return self

    def click_try_free(self):
        self.drop_down_menu.element('.menu-item-try-free').click()
        return self

    def click_remove_from_wishlist(self):
        self.drop_down_menu.element('[data-qa="menu-item-remove-from-wishlist"]').click()
        return self


class ModalDialog:
    def click_remove(self):
        button = browser.element('[data-theme="tak-confirm-danger"]').element('.modal-popup__footer') \
            .element('.danger').with_(click_by_js=True)
        button.click()
        return self


item = Item()
modal_dialog = ModalDialog()
