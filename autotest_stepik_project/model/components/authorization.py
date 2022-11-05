from selene import be
from selene.support.shared import browser


class Authorization:
    def open_authorization_popup(self):
        browser.element('.navbar').element('.navbar__auth_login').click()
        return self

    def should_be_visible_sign_form(self):
        browser.element('.sign-form').should(be.visible)
        return self

    def set_login_email(self, value):
        browser.element('#id_login_email').type(value)
        return self

    def set_password(self, value):
        browser.element('#id_login_password').type(value)
        return self

    @staticmethod
    def submit():
        browser.element('.sign-form__btn').click()
