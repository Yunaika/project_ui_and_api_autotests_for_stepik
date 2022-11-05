import time

from selene import have, be
from selene.support.shared import browser

from autotest_stepik_project.model.controls.checkbox import select_course_option
from autotest_stepik_project.utils.patching.allure.report import step


class CatalogPage:
    class Search:
        @step
        def set_text_to_search(self, value: str):
            browser.element('.search-form__input ').type(value)
            return self

        @step
        def set_with_certificate(self):
            select_course_option('With certificate')
            return self

        @step
        def set_free_course(self):
            select_course_option('Free')
            return self

        @step
        def submit(self):
            browser.element('.search-form__submit').click()
            time.sleep(10)
            return self

        @step
        def press_enter(self):
            browser.element('.search-form__input').press_enter()
            time.sleep(10)
            return self

    class SearchResult:
        class CourseCards:
            course_cards = browser.element('.course-cards').all('.course-cards__item')

            @step
            def should_have_title(self, value):
                self.course_cards.element_by_its('.course-card__title', have.exact_text(value)).should(be.visible)
                return self

            @step
            def should_have_certificate(self, value):
                self.course_cards.element_by_its('.course-card__title', have.exact_text(value)) \
                    .element('.course-card').element('.course-card__widgets') \
                    .element('[data-type="certificate"]').should(have.text('certificate'))
                return self

            @step
            def should_have_free_price(self, value):
                self.course_cards.element_by_its('.course-card__title', have.exact_text(value)) \
                    .element('.course-card').element('.course-card__price') \
                    .element('.format-price_free').should(be.visible)
                return self

        @step
        def should_have_message_text(self, value):
            browser.element('.catalog__search-results-message').should(have.text(value))
            return self

        course_cards = CourseCards()

    search = Search()
    search_result = SearchResult()
