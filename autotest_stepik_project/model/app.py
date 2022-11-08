import os
import time

from selene.support.shared import browser

from autotest_stepik_project.api_framework.stepik import stepik, stepik_url
from autotest_stepik_project.model.components import mobile_banner
from autotest_stepik_project.model.components.authorization import Authorization
from autotest_stepik_project.model.components.header_menu import HeaderMenu
from autotest_stepik_project.model.components.learning_sidebar import LearningSideBar
from autotest_stepik_project.model.pages import catalog_page
from autotest_stepik_project.model.pages.course_page import CoursePage
from autotest_stepik_project.model.pages import courses_active_page
from autotest_stepik_project.model.pages.main_page import MainPage
from autotest_stepik_project.model.pages.profile_page import ProfilePage
from autotest_stepik_project.model.pages import wishlist_page
from autotest_stepik_project.utils.patching.allure.report import step


auth = Authorization()
header_menu = HeaderMenu()
main_page = MainPage()
profile = ProfilePage()
catalog_page = catalog_page
course_page = CoursePage()
learning_sidebar = LearningSideBar()
courses_active = courses_active_page
wishlist_page = wishlist_page

@step
def given_opened_main_page():
    browser.open(stepik_url)
    time.sleep(10)

@step
def given_opened_catalog():
    mobile_banner.click_close_button()
    browser.open(f'{stepik_url}/catalog')


def given_opened_course_page(course_id):
    browser.open(f'{stepik_url}/course/{course_id}/promo')
    time.sleep(20)


def given_opened_profile_page():
    browser.open(f'{stepik_url}/users/{os.getenv("PROFILE_ID")}')


def given_opened_wishlist_page():
    browser.open(f'{stepik_url}/learn/courses/wishlist')


def given_opened_courses_active_page():
    browser.open(f'{stepik_url}/learn/courses')
    pass


@step
def authorization(user_email: str, user_password: str):
    auth.open_authorization_popup() \
        .set_login_email(user_email) \
        .set_password(user_password) \
        .submit()


def delete_course_from_wishlist(course_id):
    stepik.delete_course_from_wishlist(course_id)


def delete_course_from_enrollments(course_id):
    stepik.delete_course_from_enrollments(course_id)
