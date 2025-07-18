from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page1_home_page import HomePage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page2_search_results_page import \
    SearchResultsPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page4_contact_page import ContactPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page5_general_services_page import \
    AncillariesPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page6_flight_summary_details import \
    FlightSummaryDetails


class BaseTest:

    home_page = HomePage
    search_results_page = SearchResultsPage
    flexi_page_object = search_results_page.choose_elal_flight
    contact_page = ContactPage
    ancillaries_page = AncillariesPage
    flight_summary_details = FlightSummaryDetails