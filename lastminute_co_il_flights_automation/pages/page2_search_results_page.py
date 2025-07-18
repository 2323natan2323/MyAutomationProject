
from playwright.sync_api import Page, TimeoutError
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.base_page import BasePage



class SearchResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __FLIGHT_CARD_LIST = ".results-page-body"
    __SEARCH_RESULTS_ELEMENT = '.search-results-txt [key="Filter.SearchResults"]'
    __ELAL_FILTER_CHECK = '.right-section [value="LY"]'
    __AVAILABLE_FLIGHTS_SEGMENTS = "app-flight-card .card-container"
    __SEGMENT_OUTBOUND_FLIGHT_TEXT = ".flight-row:nth-child(1) .airline-box-name"
    __SEGMENT_INBOUND_FLIGHT_TEXT = ".flight-row:nth-child(2) .airline-box-name"
    __ORDER_FLIGHT_BTN = "app-flight-card-price-box .primary-btn"
    __CHOOSE_FLIGHT_SEARCH_RESULTS_BTN = "app-flight-search-summary .search-summary-wrapper > .search-summary"
    __DATE_PICKER = "app-datepicker .picker-container"
    __NEXT_MONTH_BTN = ".container__months .month-item:nth-child(2) .button-next-month"
    __FIND_ME_FLIGHTS_BTN = ".search-and-add-btn .primary-btn"
    __MAX_WAIT_FOR_RESULTS = 45000  # ממתין עד 45 שניות לתוצאות החיפוש

    def safe_load_search_results(self):
        """
        Ensures the search results page is loaded.
        If not, retries with alternative dates.
        """
        try:
            search_result_element = self._page.locator(self.__SEARCH_RESULTS_ELEMENT)
            search_result_element.wait_for(state="visible", timeout=30000)
            print("✅ Search results page loaded successfully!")
        except TimeoutError:
            print("❌ Search results did not load in time. Trying alternative dates...")
            self.retry_search_with_alternative_dates()

    def retry_search_with_alternative_dates(self):
        print("🔁 Trying to reload search results or retry with alternative dates...")

        # תאריכים חלופיים לנסות
        dates_to_try = [("13", "20"), ("14", "21"), ("15", "22")]

        # מוודאים אם תוצאות החיפוש הגיעו בכל זאת
        try:
            search_result_element = self._page.locator(self.__SEARCH_RESULTS_ELEMENT)
            search_result_element.wait_for(state="visible", timeout=self.__MAX_WAIT_FOR_RESULTS)
            print("✅ The search result page was loaded successfully!")
            return
        except TimeoutError:
            print("❌ Search results not found, trying to select alternative dates.")

        # לוחצים על כפתור בחירת טיסה
        try:
            self.click(self.__CHOOSE_FLIGHT_SEARCH_RESULTS_BTN)
            print("🟢 Clicked on 'Choose flight' button.")
        except Exception:
            raise AssertionError("❌ Failed to click on 'Choose flight' button.")

        # מוודאים שבורר התאריכים נפתח
        date_picker = self._page.locator(self.__DATE_PICKER)
        try:
            date_picker.wait_for(state="visible", timeout=7000)
            print("📅 Date picker opened.")
        except TimeoutError:
            raise AssertionError("❌ Date picker did not open!")

        # משתנים לזכירת התאריכים שנבחרו
        self._selected_outbound_date = None
        self._selected_inbound_date = None

        def try_select_dates(month_index: int):
            for outbound_text, inbound_text in dates_to_try:
                print(f"📆 Trying to select {outbound_text} and {inbound_text} in month index {month_index + 1}")
                outbound = self._page.locator(
                    f'.container__months .month-item:nth-child({month_index + 1}) .container__days a.day-item'
                ).filter(has_text=outbound_text)
                inbound = self._page.locator(
                    f'.container__months .month-item:nth-child({month_index + 1}) .container__days a.day-item'
                ).filter(has_text=inbound_text)

                try:
                    outbound.wait_for(state="visible", timeout=3000)
                    inbound.wait_for(state="visible", timeout=3000)
                    self.click(outbound)
                    self.click(inbound)
                    self._selected_outbound_date = outbound_text
                    self._selected_inbound_date = inbound_text
                    print(f"✅ Selected dates: {outbound_text} - {inbound_text}")
                    return True
                except TimeoutError:
                    print(f"❌ Dates {outbound_text} - {inbound_text} not found in month index {month_index + 1}")
            return False

        # ניסיון לבחור תאריכים לאורך 5 חודשים קדימה
        for i in range(5):
            if try_select_dates(month_index=i):
                break
            try:
                next_btn = self._page.locator(self.__NEXT_MONTH_BTN)
                next_btn.wait_for(state="visible", timeout=3000)
                self.click(next_btn)
                print(f"➡️ Clicked on 'Next Month' ({i + 1}/5)")
            except Exception:
                raise AssertionError("❌ Failed to click on 'Next month' button.")

        # סיכום
        if self._selected_outbound_date and self._selected_inbound_date:
            print(f"📅 Retrying search for dates: {self._selected_outbound_date} → {self._selected_inbound_date}")
        else:
            raise AssertionError("❌ Could not find any valid date combination after trying 5 months.")

        # נלחץ על "מצא לי טיסות"
        try:
            self.click(self.__FIND_ME_FLIGHTS_BTN)
            print("🔄 Retrying search with selected dates...")
        except Exception:
            raise AssertionError("❌ Failed to click on 'Find me flights' button.")

    def check_elal_airline_filter(self):
        elal_checkbox = self._page.locator(self.__ELAL_FILTER_CHECK)
        assert elal_checkbox.is_visible(), "❌ El Al filter checkbox is not visible on the page!"

        self.click(elal_checkbox)
        print("✅ El Al filter checkbox was clicked successfully.")

    def choose_elal_flight(self):
        self._page.wait_for_timeout(3000)
        print("🌐 Current URL:", self._page.url)
        print("✈️ Choosing El Al flight...")

        flight_cards_list = self._page.locator(self.__FLIGHT_CARD_LIST)
        flight_cards_list.wait_for(state="visible", timeout=10000)
        assert flight_cards_list.is_visible(), "❌ Flight search results are not visible!"
        print("✅ Flight search results are visible.")

        available_flights_segments = self._page.locator(self.__AVAILABLE_FLIGHTS_SEGMENTS)
        count = available_flights_segments.count()
        for i in range(count):
            segment = available_flights_segments.nth(i)

            elal_outbound_flight_text = segment.locator(self.__SEGMENT_OUTBOUND_FLIGHT_TEXT).first
            elal_outbound_flight_text.wait_for(state="visible", timeout=10000)
            outbound_airline_name = elal_outbound_flight_text.inner_text().strip().lower()

            elal_inbound_flight_text = segment.locator(self.__SEGMENT_INBOUND_FLIGHT_TEXT).first
            elal_inbound_flight_text.wait_for(state="visible", timeout=10000)
            inbound_airline_name = elal_inbound_flight_text.inner_text().strip().lower()

            if "el al" in outbound_airline_name:
                print("✅ El Al outbound flight found.")
            else:
                print(f"❌ El Al outbound flight not found in flight #{i + 1}")

            if "el al" in inbound_airline_name:
                print("✅ El Al inbound flight found.")
            else:
                print(f"❌ El Al inbound flight not found in flight #{i + 1}")

            if "el al" in outbound_airline_name and "el al" in inbound_airline_name:
                order_flight_btn = segment.locator(self.__ORDER_FLIGHT_BTN)
                order_flight_btn.wait_for(state="attached", timeout=10000)
                print("🟢 El Al round trip found! Booking now...")

                with self._page.context.expect_page() as flexi_page_info:
                    self.click(order_flight_btn)

                flexi_page = flexi_page_info.value
                flexi_page.wait_for_load_state()
                return flexi_page

        raise AssertionError("❌ No round trip El Al flight was found in the available search results.")






















