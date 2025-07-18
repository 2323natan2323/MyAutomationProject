from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def click(self, locator):
        resolved_locator = self._resolve(locator)
        self._highlight_element(resolved_locator)
        resolved_locator.click()

    def fill_info(self, locator, text: str):
        resolved_locator = self._resolve(locator)
        resolved_locator.fill(text)

    def get_inner_text(self, locator) -> str:
        return self._resolve(locator).inner_text()

    def _highlight_element(self, locator: Locator, color: str = "yellow"):
        locator.evaluate(f"""
            (el) => {{
                const origShadow = el.style.boxShadow;
                const origBackground = el.style.backgroundColor;

                el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
                el.style.backgroundColor = '{color}';

                setTimeout(() => {{
                    el.style.boxShadow = origShadow;
                    el.style.backgroundColor = origBackground;
                }}, 300);
            }}
        """)

    def _resolve(self, locator) -> Locator:
        if isinstance(locator, str):
            return self._page.locator(locator)
        elif isinstance(locator, Locator):
            return locator
        else:
            raise TypeError(f"Unsupported locator type: {type(locator)}")
