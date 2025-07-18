from playwright.sync_api import Page

from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.base_page import BasePage


class AncillariesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __PREMIUM_FLEX_SERVICE_PACKAGE = "app-service-card:nth-child(1) .head"
    __PREMIUM_FLEX_SERVICE_PACKAGE_CHOOSE_BTN = "app-service-card:nth-child(1) .card-header-container .radio-circle"
    __CANCELLATION_PROTECTION = "app-service-card:nth-child(2) .head"
    __CANCELLATION_PROTECTION_BTN = "app-service-card:nth-child(2) .card-header-container .radio-circle"
    __BAGGAGE_PROTECTION = "app-service-card:nth-child(3) .head"
    __BAGGAGE_PROTECTION_BTN = "app-service-card:nth-child(3) .card-header-container .radio-circle"
    __ANCILLARIES_CONTINUE_BTN = ".btn-container > .primary-btn"

    def choose_ancillaries(self):
        # Premium Flex Package
        premium_flex = self._page.locator(self.__PREMIUM_FLEX_SERVICE_PACKAGE)
        premium_flex.wait_for(state="visible", timeout=30000)
        premium_flex_text = premium_flex.inner_text()
        if "חבילת שירות פרמיום מותאמת לעידן השינויים והביטולים" in premium_flex_text:
            premium_flex_btn = self._page.locator(self.__PREMIUM_FLEX_SERVICE_PACKAGE_CHOOSE_BTN)
            premium_flex_btn.wait_for(state="visible", timeout=30000)
            assert premium_flex_btn.is_visible(), "❌ Premium Flex service button not found!"
            self.click(premium_flex_btn)
            print("✅ Clicked on 'Premium Flex service' button.")

        # Cancellation Protection
        cancellation_protection = self._page.locator(self.__CANCELLATION_PROTECTION)
        cancellation_protection.wait_for(state="visible", timeout=30000)
        cancellation_protection_text = cancellation_protection.inner_text()
        if "להזמין בראש שקט" in cancellation_protection_text:
            cancellation_btn = self._page.locator(self.__CANCELLATION_PROTECTION_BTN)
            cancellation_btn.wait_for(state="visible", timeout=30000)
            assert cancellation_btn.is_visible(), "❌ 'Cancellation protection' button not found!"
            self.click(cancellation_btn)
            print("✅ Clicked on 'Cancellation protection' button.")

        # Baggage Protection
        baggage_protection = self._page.locator(self.__BAGGAGE_PROTECTION)
        baggage_protection.wait_for(state="visible", timeout=30000)
        baggage_text = baggage_protection.inner_text()
        if "מזוודה שאבדה יכולה להרוס נסיעה" in baggage_text:
            baggage_btn = self._page.locator(self.__BAGGAGE_PROTECTION_BTN)
            baggage_btn.wait_for(state="visible", timeout=30000)
            assert baggage_btn.is_visible(), "❌ 'Baggage protection' button not found!"
            self.click(baggage_btn)
            print("✅ Clicked on 'Baggage protection' button.")

        # Continue Button
        self._page.wait_for_timeout(1000)
        continue_btn = self._page.locator(self.__ANCILLARIES_CONTINUE_BTN)
        continue_btn.wait_for(state="visible", timeout=30000)
        assert continue_btn.is_visible(), "❌ 'Continue' button not found on ancillaries page!"
        self.click(continue_btn)
        print("➡️ Clicked on 'Continue' button to proceed.")
