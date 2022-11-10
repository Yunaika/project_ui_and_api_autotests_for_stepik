from selene import have, be
from selene.support.shared import browser


class Item:
    def should_have_title(self, value: str):
        browser.element('.item-tile-list').all('.item-tile') \
            .element_by_its('.item-tile__title', have.exact_text(value)).should(be.visible)
        return self


class CoursesActivePage:
    def __init__(self):
        self.item = Item()
