from selene import be
from selene.support.shared import browser

from autotest_stepik_project.utils.patching.allure.report import step


class MainPage:
    @step
    def should_be_visible_news_modal_dialog(self):
        browser.element('.modal-dialog-inner').should(be.visible)
        return self
