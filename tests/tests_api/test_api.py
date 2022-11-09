import copy
import os

import allure
from allure_commons.types import Severity

from autotest_stepik_project.framework_api.stepik import stepik
from data.user_data import user, user_profile_data
from data.schemas.stepik_api_schemas import course_lists_schema
from pytest_voluptuous import S


@allure.tag("api")
@allure.label('owner', 'juliamur')
@allure.feature('API')
@allure.story('Authorization')
class TestsAuthorizationApi:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Authorization succeeded with OAuth 2.0 by registered user')
    def test_successful_authorization_with_oauth2_by_registered_user(self):
        # WHEN
        response = stepik.login_oauth2_and_get_token(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

        # THEN
        assert response.status_code == 200


    @allure.severity(Severity.CRITICAL)
    @allure.title('Authorization with OAuth 2.0 with incorrect password')
    def test_unsuccessful_authorization_with_incorrect_password(self):
        # WHEN
        response = stepik.login_oauth2_and_get_token(os.getenv('CLIENT_ID'), 'bad password')

        # THEN
        assert response.status_code == 401


    @allure.severity(Severity.CRITICAL)
    @allure.title('Authorization with OAuth 2.0 by nonexistent user')
    def test_unsuccessful_authorization_by_nonexistent_user(self):
        # WHEN
        response = stepik.login_oauth2_and_get_token('nonexistent user', 'bad password')

        # THEN
        assert response.status_code == 401


@allure.tag("api")
@allure.label('owner', 'juliamur')
@allure.feature('API')
@allure.story('Course list')
class TestsCourseList:
    @allure.severity(Severity.NORMAL)
    @allure.title('Get course list by topic')
    def test_get_course_list_by_topic(self):
        # PRECONDITION
        course_list_number = 219

        # WHEN
        response = stepik.get_course_list(course_list_number)

        # THEN
        assert response.status_code == 200
        assert S(course_lists_schema) == response.json()
        assert response.json()['course-lists'][0]['id'] == course_list_number
        assert str(response.json()['course-lists'][0]['title']) == 'Тестирование ПО'
        assert str(response.json()['course-lists'][0]['language']) == 'ru'


@allure.tag("api")
@allure.label('owner', 'juliamur')
@allure.feature('API')
@allure.story('Profile')
class TestsProfile:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Get registered user profile info')
    def test_get_registered_user_profile_info(self):
        # PRECONDITION
        profile_id = os.getenv('PROFILE_ID')

        # WHEN
        response = stepik.get_profile_info(profile_id)

        # THEN
        assert response.status_code == 200
        assert str(response.json()['users'][0]['id']) == user['id']
        assert str(response.json()['users'][0]['first_name']) == user['first_name']
        assert str(response.json()['users'][0]['last_name']) == user['last_name']
        assert str(response.json()['users'][0]['avatar']) == user['avatar']
        assert str(response.json()['users'][0]['details']) == user['details']


    @allure.severity(Severity.CRITICAL)
    @allure.title('Get nonexistent user profile info')
    def test_get_nonexistent_user_profile_info(self):
        # PRECONDITION
        profile_id = 5644646454654

        # WHEN
        response = stepik.get_profile_info(profile_id)

        # THEN
        assert response.status_code == 404


    @allure.severity(Severity.CRITICAL)
    @allure.title('Update registered user first name')
    def test_update_user_first_name(self):
        # PRECONDITION
        profile_id = os.getenv('PROFILE_ID')
        new_name = 'New test name'
        data = copy.deepcopy(user_profile_data)
        data['profile']['first_name'] = new_name

        # WHEN
        update_profile = stepik.update_profile_info(profile_id, data)
        response = stepik.get_profile_info(profile_id)

        # THEN
        assert update_profile.status_code == 200
        assert response.status_code == 200
        assert str(response.json()['users'][0]['first_name']) == new_name
        assert str(response.json()['users'][0]['last_name']) == 'profile'

        # POSTCONDITION
        update_profile = stepik.update_profile_info(profile_id, user_profile_data)
        response = stepik.get_profile_info(profile_id)
        assert update_profile.status_code == 200
        assert response.status_code == 200
        assert str(response.json()['users'][0]['first_name']) == 'Test'
