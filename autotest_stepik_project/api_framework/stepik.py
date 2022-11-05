import json
import os

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from autotest_stepik_project.utils.patching.requests.BaseSession import BaseSession

load_dotenv()
stepik_url = os.getenv('BASE_URL')


class Stepik:
    def __init__(self):
        self.stepik = BaseSession(base_url=stepik_url)

    def get_token(self):
        response = self.login_oauth2_and_get_token(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
        return json.loads(response.text)['access_token']

    def login_oauth2_and_get_token(self, client_id: str, client_secret: str):
        auth = HTTPBasicAuth(client_id, client_secret)
        response = self.stepik.post('/oauth2/token/',
                                    data={'grant_type': 'client_credentials'},
                                    auth=auth,
                                    allow_redirects=False
                                    )
        return response

    def get_course_list(self, course_list_number: int):
        return self.stepik.get(f'/api/course-lists/{course_list_number}')

    def get_course_name(self, id: int) -> str:
        course_info = self.stepik.get(f'/api/courses/{id}')
        return course_info.json()['courses'][0]['title']

    def get_profile_info(self, profile_id: int):
        return self.stepik.get(f'/api/users/{profile_id}')

    def update_profile_info(self, profile_id: int, data: dict):
        return self.stepik.put(f'/api/profiles/{profile_id}',
                               headers={'Authorization': 'Bearer ' + self.get_token()}, json=data)

    def get_user_wish_list(self):
        return self.stepik.get('/api/wish-lists/',
                               headers={'Authorization': 'Bearer ' + self.get_token()}).json()['wish-lists']

    def delete_course_from_wishlist(self, id_course_to_be_deleted: int):
        user_wish_list = self.get_user_wish_list()
        for wish_list in user_wish_list:
            if wish_list['course'] == id_course_to_be_deleted:
                id_courses_in_wish_list = wish_list['id']
                break
        response = self.stepik.delete(f'/api/wish-lists/{id_courses_in_wish_list}',
                                      headers={'Authorization': 'Bearer ' + self.get_token()})
        # assert response.status_code == 204
        return response

    def get_user_enrollments(self):
        return self.stepik.get('/api/enrollments',
                               headers={'Authorization': 'Bearer ' + self.get_token()})

    def delete_course_from_enrollments(self, id_course_to_be_deleted: int):
        user_enrollments = self.get_user_enrollments()
        for enrollment in user_enrollments.json()['enrollments']:
            if enrollment['course'] == id_course_to_be_deleted:
                id_courses_in_enrollments = enrollment['id']
                break
        return self.stepik.delete(f'/api/enrollments/{id_course_to_be_deleted}',
                                  headers={'Authorization': 'Bearer ' + self.get_token()})
        # assert response.status_code == 204
        return response

    def logout(self):
        return self.stepik.post('/api/users/logout')


stepik = Stepik()
