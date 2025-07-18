import pytest
from playwright.sync_api import sync_playwright

from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page1_home_page import HomePage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page2_search_results_page import \
    SearchResultsPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page3_flexi_page import FlexiPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.tests.base_test import BaseTest


class TestFlightBooking(BaseTest):
    def test_homepage_to_step2_flexi(self, page):

        contact_first_name = "Test"
        contact_last_name = "Prod"
        email = "natan@lastminute.co.il"
        confirmation_email = "natan@lastminute.co.il"
        phone_number = "0527491280"
        birthday_date = "23111999"
        passenger_first = "Natan"
        passenger_last = "Shor"
        passenger_full_name = f"{passenger_first} {passenger_last}"
        passenger_gender = "זכר"

        page.goto("https://www.lastminute.co.il/")


        self.home = HomePage(page)
        self.home.safe_landing()
        self.home.close_cookies_message()
        self.home.click_flight_tab()
        self.home.set_trip_direction()
        self.home.set_passenger_type_and_count()
        self.home.set_flight_class()
        self.home.choose_outbound_flight("תל אביב")
        self.home.choose_inbound_flight("אתונה")
        self.home.set_flight_dates()
        self.search = SearchResultsPage(page)
        self.search.safe_load_search_results()
        self.search.retry_search_with_alternative_dates()
        self.search.check_elal_airline_filter()
        self.search.choose_elal_flight()
        new_tab = self.search.choose_elal_flight()
        self.flexi = FlexiPage(new_tab)
        self.flexi.wait_for_page_to_load()
        self.flexi.choose_flexi_ticket()


