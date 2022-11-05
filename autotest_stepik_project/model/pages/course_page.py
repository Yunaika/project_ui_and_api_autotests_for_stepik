from selene import have, be
from selene.support.shared import browser


class CoursePage:
    def add_course_in_wishlist(self):
        if browser.element('.course-promo__aside-sticky-wrapper').matching(be.visible):
            browser.element('.course-promo__aside-sticky-wrapper') \
                   .element('.course-promo-enrollment__wishlist-btn') \
                   .click()
        else:
            browser.element('[data-appearance="mobile-bottom-panel"]') \
                   .element('.course-promo-enrollment__wishlist-btn') \
                   .click()

        return self

    def join_the_course(self):
        browser.element('.course-promo-enrollment__join-btn').click()
        return self
