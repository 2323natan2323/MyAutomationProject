

from playwright.sync_api import Page
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.base_page import BasePage


class FlexiPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __FLEXI_PAGE_ELEMENT = ".step-button.current > .btn-title"
    __FLEXI_BTN = ".option-card-container.premium .call-to-action .secondary-btn"

    def wait_for_page_to_load(self):
        self._page.wait_for_load_state()
        print("🌐 Current URL:", self._page.url)

        flexi_page_element = self._page.locator(self.__FLEXI_PAGE_ELEMENT)
        flexi_page_element.wait_for(state="visible", timeout=100000)

        assert flexi_page_element.is_visible(), "❌ Flexi page did not load!"
        print("✅ Flexi page loaded successfully.")

    def choose_flexi_ticket(self):
        flexi_btn = self._page.locator(self.__FLEXI_BTN)
        flexi_btn.wait_for(timeout=20000)

        assert flexi_btn.is_visible(), "❌ Flexi ticket button was not found!"
        print("✅ Flexi ticket button is visible. Clicking now...")
        self.click(flexi_btn)








