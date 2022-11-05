import os
import allure
import pytest

from allure_commons.types import Severity
from autotest_stepik_project.api_framework.stepik import stepik
from autotest_stepik_project.model import app
from data.user_data import user_info

user_email = os.getenv('LOGIN')
user_password = os.getenv('PASSWORD')


@allure.tag("ui", "web")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('Authorization')
class TestsAuthorization:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Authorization succeeded by registered user')
    @pytest.mark.parametrize('window_size', ['desktop', 'tablet', 'mobile'], indirect=True)
    def test_authorization_succeeded_by_registered_user(self, setup_browser):
        # PRECONDITION
        user_id = user_info['id']
        user_full_name = user_info['full_name']

        # WHEN
        with allure.step('Open main page'):
            app.given_opened_main_page()

        with allure.step('Open authorization popup'):
            app.auth.open_authorization_popup()

        with allure.step('Set email'):
            app.auth.set_login_email(user_email)

        with allure.step('Set password'):
            app.auth.set_password(user_password)

        with allure.step('Click submit'):
            app.auth.submit()

        # THEN
        with allure.step('Open profile page'):
            app.given_opened_profile_page()

        with allure.step('Check profile name'):
            app.profile.should_have_profile_name(user_full_name)

        with allure.step('Check profile id'):
            app.profile.should_have_profile_id(user_id)


@allure.tag("ui", "web")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('Wishlist')
class TestsWishlist:
    @allure.severity(Severity.NORMAL)
    @allure.title('Add course to wishlist')
    @pytest.mark.parametrize('window_size', ['desktop', 'tablet', 'mobile'], indirect=True)
    def test_add_course_to_wishlist(self, setup_browser, course_id=95367):
        # PRECONDITION
        with allure.step('Get course name'):
            course_name = stepik.get_course_name(course_id)

        # WHEN
        with allure.step('Open course page'):
            app.given_opened_course_page(course_id)
        with allure.step('Authorization'):
            app.authorization(user_email, user_password)
        with allure.step('Add course in wishlist'):
            app.course_page.add_course_in_wishlist()

        # THEN
        with allure.step('Open wishlist page'):
            app.given_opened_wishlist_page()
        with allure.step(f'Courses list must contain the course "{course_name}"'):
            app.wishlist_page.item.should_have_title(course_name)

        # POSTCONDITION
        with allure.step('Delete course from wishlist'):
            app.delete_course_from_wishlist(course_id)


@allure.tag("ui", "web")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('Join the course')
class TestsJoinCourse:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Join the free course with authorization')
    @pytest.mark.parametrize('window_size', ['desktop'], indirect=True)
    def test_join_the_free_course_with_authorization(self, setup_browser, course_id=3356):
        # PRECONDITION
        with allure.step('Get course name'):
            course_name = stepik.get_course_name(course_id)

        # WHEN
        with allure.step('Open course page'):
            app.given_opened_course_page(course_id)

        with allure.step('Authorization'):
            app.authorization(user_email, user_password)

        with allure.step('Join the course'):
            app.course_page.join_the_course()

        # THEN
        with allure.step('Open active courses page'):
            app.given_opened_courses_active_page()
        with allure.step(f'Courses list must contain the course "{course_name}"'):
            app.courses_active.item.should_have_title(course_name)

        # POSTCONDITION
        with allure.step('Delete course from active courses'):
            app.delete_course_from_enrollments(course_id)

    @allure.severity(Severity.NORMAL)
    @allure.title('Join the free course without authorization')
    @pytest.mark.parametrize('window_size', ['desktop'], indirect=True)
    def test_join_the_free_course_without_authorization(self, setup_browser, course_id=3356):
        # WHEN
        with allure.step('Open course page'):
            app.given_opened_course_page(course_id)

        with allure.step('Click "Join the course" button'):
            app.course_page.join_the_course()

        # THEN
        with allure.step('Should be visible sign form'):
            app.auth.should_be_visible_sign_form()


@allure.tag("ui", "web")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('Search')
class TestsSearch:
    @allure.severity(Severity.NORMAL)
    @allure.title('Search free course with certificate')
    @pytest.mark.parametrize('window_size', ['desktop'], indirect=True)
    def test_search_free_course_with_certificate(self, setup_browser, search_query='Инди-курс программирования на Python'):
        # WHEN
        app.given_opened_catalog()

        app.catalog_page.search.set_text_to_search(search_query)\
            .set_with_certificate()\
            .set_free_course()\
            .submit()

        # THEN

        app.catalog_page.search_result.course_cards.should_have_title(search_query)\
            .should_have_certificate(search_query)\
            .should_have_free_price(search_query)

    @allure.tag("ui", "web")
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'juliamur')
    @allure.feature('UI')
    @allure.story('Search')
    @allure.title('Search nonexistent course')
    @pytest.mark.parametrize('window_size', ['mobile'], indirect=True)
    def test_search_nonexistent_course(self, setup_browser, course_name='uberlebenskurs'):
        # WHEN
        app.given_opened_catalog()

        app.catalog_page.search.set_text_to_search(course_name)\
                               .press_enter()

        # THEN
        app.catalog_page.search_result.should_have_message_text(course_name)


@allure.tag("ui", "web")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('News')
class TestsNews:
    @allure.severity(Severity.NORMAL)
    @allure.title('Open news popup window from the header menu')
    @pytest.mark.parametrize('window_size', ['desktop'], indirect=True)
    def test_open_news_popup_window_from_the_menu(self, setup_browser):
        # WHEN
        app.given_opened_main_page()

        app.authorization(user_email, user_password)

        app.header_menu.click_on_profile_icon()
        app.header_menu.drop_down_profile_menu.click_on_news()

        # THEN
        app.main_page.should_be_visible_news_modal_dialog()
