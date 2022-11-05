from selene import have
from selene.support.shared import browser


class ProfilePage:
    def should_have_profile_name(self, value: str):
        browser.element('.profile-header-widget__name').should(have.exact_text(value))
        return self

    def should_have_profile_id(self, value: int | str):
        browser.element('.profile-aside-widget').all('p').second.should(have.text('531000954'))
        return self
