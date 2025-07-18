from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def click(self, locator):

        if isinstance(locator, str):
            self._page.locator(locator).highlight()
        elif isinstance(locator, Locator):
            locator.highlight()

        if isinstance(locator, str):
            self._page.locator(locator).click()
        elif isinstance(locator, Locator):
            locator.click()

    def fill_info(self, locator, text):
        if isinstance(locator, str):
            self._page.locator(locator).fill(text)
        elif isinstance(locator, Locator):
            locator.fill(text)

    def get_inner_text(self, locator):
        return self._page.locator(locator).inner_text()

