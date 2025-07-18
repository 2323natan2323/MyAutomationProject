import pytest
from playwright.sync_api import sync_playwright

from automation.lastminute_automation.lastminute_co_il_flights_automation.tests.base_test import BaseTest
from automation.lastminute_automation.utils.config import ConfigReader
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page1_home_page import HomePage


class TestFlightBooking(BaseTest):

    def test_homepage(self, page):

        # 1. Contact & Passenger data
        contact_first_name = "Test"
        contact_last_name = "Prod"
        email = "natan@lastminute.co.il"
        phone_number = "0527491280"
        birthday = "23111999"
        passenger_first = "Natan"
        passenger_last = "Shor"
        full_name = f"{passenger_first} {passenger_last}"
        gender = "זכר"

        page.goto("https://www.lastminute.co.il")

        # 2. Home Page
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
