from playwright.sync_api import Page
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.base_page import BasePage
class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)


    __FLIGHT_TAB = "app-search-tabs .options> .option:nth-child(2)"
    __TRIP_TYPE_DROPDOWN = ".direction-tabs app-dropdown .dropdown-container"
    __COOKIES_MESSAGE_CLOSE_BTN = ".message-container.right.bottom .primary-btn"
    __ROUND_TRIP_BTN = ".direction-tabs app-dropdown .option:nth-child(1)"
    __ONE_WAY_TRIP = ".direction-tabs app-dropdown .options-container.dropdown.show div:nth-child(2)"
    __MULTI_WAY = ".direction-tabs app-dropdown .options-container.dropdown.show div:nth-child(3)"
    __PASSENGER_DROPDOWN = "app-passengers-dropdown .label-input"
    __REDUCE_NUMBER_OF_ADULT_BTN = "app-passengers-dropdown .option-row:nth-child(1) .btn-section>div:nth-child(1)"
    __INCREASE_NUMBER_OF_ADULT_BTN = "app-passengers-dropdown .option-row:nth-child(1) .btn-section .square.icon-lm-plus"
    __PASSENGER_DROPDOWN_CONFIRMATION_BTN = ".paxs-options-container.dropdown .btn-container .primary-btn"
    __FLIGHT_CLASS_DROPDOWN = "app-flight-search .top-inputs-container>app-dropdown .dropdown-container"
    __ECONOMY_CLASS = "app-flight-search .top-inputs-container>app-dropdown .options-container.dropdown.show .option:nth-child(1)"
    __PREMIUM_CLASS = "app-flight-search .top-inputs-container>app-dropdown .options-container.dropdown.show .option:nth-child(2)"
    __BUSINESS_CLASS = "app-flight-search .top-inputs-container>app-dropdown .options-container.dropdown.show .option:nth-child(3)"
    __FIRST_CLASS = "app-flight-search .top-inputs-container>app-dropdown .options-container.dropdown.show .option:nth-child(4)"
    __CHOOSE_OUTBOUND_FLIGHT_BTN = ".destinations-container app-flights-autocomplete:nth-child(1) .input-wrapper"
    __OUTBOUND_FLIGHT_CITY_TITLE = ".destinations-container app-flights-autocomplete:nth-child(1) .input-wrapper .text-input"
    __ACTUAL_OUTBOUND_CITY = ".destinations-container app-flights-autocomplete:nth-child(1) .input-wrapper .option-item:nth-child(1) .main-text"
    __CHOOSE_INBOUND_FLIGHT_BTN = ".destinations-container app-flights-autocomplete:nth-child(2) .input-wrapper"
    __INBOUND_FLIGHT_CITY_TITLE = ".destinations-container app-flights-autocomplete:nth-child(2) .input-wrapper .text-input"
    __ACTUAL_INBOUND_CITY = ".destinations-container app-flights-autocomplete:nth-child(2) .input-wrapper .option-item:nth-child(1) .main-text"
    __DATE_PICKER_ELEMENT = ".tab-date.selected"
    __NEXT_MONTH_BTN = ".container__months .month-item:nth-child(2) .button-next-month"
    __PREVIOUS_MONTH_BTN = ".container__months .month-item:nth-child(1) .button-previous-month"
    __FIND_ME_FLIGHTS_BTN = ".search-and-add-btn .primary-btn"



    def close_cookies_message(self):

        home_page_cookies_message = self._page.locator(self.__COOKIES_MESSAGE_CLOSE_BTN)
        home_page_cookies_message.wait_for(state="visible", timeout=30000)
        assert home_page_cookies_message.is_visible(), "❌ The home page cookies message wasn't found!"
        self.click(self.__COOKIES_MESSAGE_CLOSE_BTN)
        print("✅ The cookies message was closed successfully!")

    # def click_flight_tab(self):
    #     flight_tab = self._page.locator(self.__FLIGHT_TAB)
    #     flight_tab.wait_for(state="visible", timeout=30000)
    #     assert flight_tab.is_visible(), "❌ The flight tab wasn't found!"
    #     self.click(self.__FLIGHT_TAB)
    #     print("✅ The flight tab was clicked successfully")

    def set_trip_direction(self):  # Set the trip direction
        print("Set the trip direction to round-trip")
        trip_type_dropdown = self._page.locator(self.__TRIP_TYPE_DROPDOWN)
        trip_type_dropdown.wait_for(state="visible", timeout=30000)
        assert trip_type_dropdown.is_visible(), "❌ The trip type dropdown wasn't found!"
        print("✅ The trip type dropdown found successfully!")


        trip_type_options = {

            "Round trip": self.__ROUND_TRIP_BTN,
            "One way": self.__ONE_WAY_TRIP,
            "Multi-city": self.__MULTI_WAY,

        }

        for trip_name, trip_selector in trip_type_options.items():
            self.click(trip_type_dropdown)
            self._page.locator(trip_selector).wait_for(state="visible", timeout=30000)
            self.click(trip_selector)
            print(f"✅ Selected trip type option: {trip_name}")

        
        self.click(self.__TRIP_TYPE_DROPDOWN)
        round_trip_option = self._page.locator(self.__ROUND_TRIP_BTN)
        round_trip_option.wait_for(state="visible", timeout= 30000)
        self.click(round_trip_option)
        print("🔁 Returned to Round Trip as final selection.")

        #assertion round trip was really chosen
        round_trip_class = self._page.locator(self.__ROUND_TRIP_BTN).get_attribute("class")
        assert "selected" in round_trip_class, f"❌ Round trip not selected! Current class: {round_trip_class}"
        print("✅ Round trip option is selected.")

    def set_passenger_type_and_count(self):
        adjust_passenger_count = [
            self.__REDUCE_NUMBER_OF_ADULT_BTN,
            self.__REDUCE_NUMBER_OF_ADULT_BTN,
            self.__INCREASE_NUMBER_OF_ADULT_BTN,
        ]

        passenger_dropdown = self._page.locator(self.__PASSENGER_DROPDOWN)
        passenger_dropdown.wait_for(state="visible", timeout=10000)
        assert passenger_dropdown.is_visible(), "❌ Passenger dropdown is not visible!"
        self.click(self.__PASSENGER_DROPDOWN)
        print("✅ The passenger dropdown was clicked successfully!")

        for button in adjust_passenger_count:
            self._page.locator(button).wait_for(state="visible", timeout=10000)
            self.click(button)

        passenger_dropdown_confirmation_btn = self._page.locator(self.__PASSENGER_DROPDOWN_CONFIRMATION_BTN)
        passenger_dropdown_confirmation_btn.wait_for(state="visible", timeout=10000)
        assert passenger_dropdown_confirmation_btn.is_visible(), "❌ Passenger dropdown confirmation btn is not visible!"
        self.click(self.__PASSENGER_DROPDOWN_CONFIRMATION_BTN)
        print("✅ The passenger dropdown confirmation btn was clicked successfully!")


    def set_flight_class(self):
        flight_classes = {
            "Economy": self.__ECONOMY_CLASS,
            "Premium": self.__PREMIUM_CLASS,
            "Business": self.__BUSINESS_CLASS,
            "First": self.__FIRST_CLASS,
        }

        for flight_name, flight_selector in flight_classes.items():
            flight_class_dropdown = self._page.locator(self.__FLIGHT_CLASS_DROPDOWN)
            flight_class_dropdown.wait_for(state="visible", timeout=10000)
            assert flight_class_dropdown.is_visible(), "❌ The flight class dropdown is not visible!"

            self.click(self.__FLIGHT_CLASS_DROPDOWN)
            dropdown_options = self._page.locator("app-flight-search .top-inputs-container>app-dropdown .options-container.dropdown.show")
            dropdown_options.wait_for(state="visible", timeout=10000)

            print("✅ The flight class dropdown was clicked successfully")
            self._page.locator(flight_selector).wait_for(state="visible", timeout=10000)
            self.click(flight_selector)
            print(f"✅ Selected flight class option: {flight_name}")

        self.click(self.__FLIGHT_CLASS_DROPDOWN)
        economy_class = self._page.locator(self.__ECONOMY_CLASS)
        economy_class.wait_for(state="visible", timeout=30000)
        assert economy_class.is_visible(), "❌ Economy class is not visible!"
        self.click(economy_class)
        print("✅ Economy class was chosen successfully!")

    def choose_outbound_flight(self, outbound_city):
        print("Selecting outbound flight")
        choose_outbound_flight_btn = self._page.locator(self.__CHOOSE_OUTBOUND_FLIGHT_BTN)
        choose_outbound_flight_btn.wait_for(state="visible", timeout=10000)
        assert choose_outbound_flight_btn.is_visible(), "❌ The outbound flight btn is not visible!"
        self.click(choose_outbound_flight_btn)
        print("✅ The outbound flight btn was clicked successfully!")

        self.fill_info(self.__OUTBOUND_FLIGHT_CITY_TITLE, outbound_city)
        actual_outbound_city = self._page.locator(self.__ACTUAL_OUTBOUND_CITY)
        actual_outbound_city.wait_for(state="visible", timeout=10000)
        actual_outbound_city_text = self._page.locator(self.__ACTUAL_OUTBOUND_CITY).inner_text()

        assert outbound_city in actual_outbound_city_text, f"❌ '{outbound_city}' not found in the outbound city title!"
        print(f"✅ '{outbound_city}' found in outbound city title.")

        self.click(self.__ACTUAL_OUTBOUND_CITY)


    def choose_inbound_flight(self, inbound_city):
        print("Selecting inbound flight")
        choose_inbound_flight_btn = self._page.locator(self.__CHOOSE_INBOUND_FLIGHT_BTN)
        choose_inbound_flight_btn.wait_for(state="visible", timeout=10000)
        assert choose_inbound_flight_btn.is_visible(), "❌ The inbound flight btn is not visible!"
        self.click(self.__CHOOSE_INBOUND_FLIGHT_BTN)
        print("✅ The inbound flight btn was clicked successfully!")

        self.fill_info(self.__INBOUND_FLIGHT_CITY_TITLE, inbound_city)
        actual_inbound_city_text = self.get_inner_text(self.__ACTUAL_INBOUND_CITY)
        assert inbound_city in actual_inbound_city_text, f"❌ '{inbound_city}' not found in the inbound city title!"
        self.click(self.__ACTUAL_INBOUND_CITY)

    def set_flight_dates(self):

        print("Set outbound and inbound dates!!")
        date_picker_element = self.__DATE_PICKER_ELEMENT
        assert self._page.locator(date_picker_element).is_visible(), "❌ The date picker element is not visible!"
        print("✅ Flight date picker element found!")

        months_btn = [
            self.__NEXT_MONTH_BTN,
            self.__NEXT_MONTH_BTN,
            self.__PREVIOUS_MONTH_BTN,
            self.__PREVIOUS_MONTH_BTN,
            self.__NEXT_MONTH_BTN,
            self.__NEXT_MONTH_BTN,
            self.__NEXT_MONTH_BTN,
            self.__NEXT_MONTH_BTN

        ]

        for btn in months_btn:
            self._page.locator(btn).wait_for(state="visible", timeout=10000)
            self.click(btn)


        outbound_day12_flight = self._page.locator('.container__months .month-item:nth-child(1) .container__days a.day-item').filter(has_text="12")
        assert outbound_day12_flight.is_visible(), "❌ The flight on the 12th is not visible!"
        print("✅ The flight on the 12th was chosen successfully!")
        self.click(outbound_day12_flight)

        inbound_day19_flight = self._page.locator('.container__months .month-item:nth-child(1) .container__days a.day-item').filter(has_text="19")
        assert inbound_day19_flight.is_visible(), "❌ The flight on the 19th is not visible!"
        print("✅ The flight on the 19th was chosen successfully!")
        self.click(inbound_day19_flight)

        find_me_flight_btn = self._page.locator(self.__FIND_ME_FLIGHTS_BTN)
        find_me_flight_btn.wait_for(state="visible", timeout=30000)
        assert find_me_flight_btn.is_visible(), "❌ Find me flights btn is not visible!"
        self.click(find_me_flight_btn)
        print("✅ Flight me flights btn was clicked successfully!")

        print("✅ Flight dates were set successfully!")


