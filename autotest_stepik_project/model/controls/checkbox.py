from selene import have
from selene.support.shared import browser


def select_course_option(value: str):
    browser.element('.search-form__form').all('.form-checkbox').element_by(have.exact_text(value)).click()
