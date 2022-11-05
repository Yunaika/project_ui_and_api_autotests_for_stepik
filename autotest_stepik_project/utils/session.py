import os

from autotest_stepik_project.utils.patching.requests.BaseSession import BaseSession


def stepik() -> BaseSession:
    stepik_url = os.getenv('BASE_URL')
    return BaseSession(base_url=stepik_url)
