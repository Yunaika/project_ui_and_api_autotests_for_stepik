from selene.support.shared import browser


class LearningSideBar:
    def click_on_item_courses_active(self):
        browser.element('[data-item="courses-active"]').click()
        return self

    def click_on_the_item_courses_wishlist(self):
        browser.element('[data-item="courses-wishlist"]').click()
        return self
