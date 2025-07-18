import pytest
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page1_home_page import HomePage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page2_search_results_page import SearchResultsPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page3_flexi_page import FlexiPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page4_contact_page import ContactPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page5_general_services_page import AncillariesPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page6_flight_summary_details import FlightSummaryDetails


@pytest.mark.usefixtures("page")
class TestFlightBooking:

    def test_flight_sanity_flow(self, page):
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

        # 2. Home Page
        home = HomePage(page)
        home.close_cookies_message()
        home.click_flight_tab()
        home.set_trip_direction()
        home.set_passenger_type_and_count()
        home.set_flight_class()
        home.choose_outbound_flight("תל אביב")
        home.choose_inbound_flight("אתונה")
        home.set_flight_dates()

        # 3. Search Page
        search = SearchResultsPage(page)
        search.safe_load_search_results()
        search.retry_search_with_alternative_dates()
        search.check_elal_airline_filter()
        flexi_page_object = search.choose_elal_flight()

        # 4. Flexi Page
        flexi = FlexiPage(flexi_page_object)
        flexi.wait_for_page_to_load()
        flexi.choose_flexi_ticket()

        # 5. Contact Page
        contact = ContactPage(flexi_page_object)
        contact.wait_for_contact_page_to_load()
        contact.fill_contact_info(contact_first_name, contact_last_name, email, email, phone_number)
        contact.fill_passenger_info(passenger_first, passenger_last, birthday)
        contact.add_outbound_baggage()
        contact.add_inbound_baggage()
        contact.continue_to_next_page_with_recovery(
            contact_first_name, contact_last_name,
            passenger_first, passenger_last,
            email, email,
            phone_number, birthday
        )

        # 6. Ancillaries
        ancillaries = AncillariesPage(flexi_page_object)
        ancillaries.choose_ancillaries()

        # 7. Summary
        summary = FlightSummaryDetails(flexi_page_object)
        summary.wait_for_summary_page_to_load()
        summary.verify_contact_details(contact_first_name, contact_last_name, phone_number, email)
        summary.verify_passenger_details(full_name, gender, birthday)
        summary.check_remark_quantity()
        summary.verify_general_services(
            "מזוודה לבטן המטוס",
            "כרטיס גמיש +",
            "חבילת שירות פרמיום מותאמת לעידן השינויים והביטולים",
            "להזמין בראש שקט",
            "מזוודה שאבדה יכולה להרוס נסיעה"
        )
        summary.choose_credit_card_payments()
        summary.fill_credit_card_first_info("Natan", "Shor", email, phone_number)
        summary.verify_flight_price()
        summary.agree_and_pay()
        summary.fill_credit_card_details("5111565657768778", "345", "209596959")

