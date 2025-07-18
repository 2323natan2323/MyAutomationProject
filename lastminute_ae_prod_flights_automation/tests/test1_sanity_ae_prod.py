from playwright.sync_api import sync_playwright

from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.page1_home_page import HomePage
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.page2_search_results_page import \
    SearchResultsPage
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.page3_flexi_page import FlexiPage
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.page4_contact_page import ContactPage
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.page5_general_services_page import \
    AncillariesPage
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.page6_flight_summary_details import \
    FlightSummaryDetails

p = sync_playwright().start()

browser = p.chromium.launch(headless=False,



    args=[
        "--start-maximized",
        "--disable-web-security",
        "--allow-running-insecure-content",
        # merged cookie + isolation overrides:
        "--disable-features=IsolateOrigins,SitePerProcess,SameSiteByDefaultCookies,BlockThirdPartyCookies",
        "--disable-blink-features=AutomationControlled"
    ],
    # drop Playwright’s own “enable-automation” switch
    ignore_default_args=["--enable-automation"]
)

context = browser.new_context(
    no_viewport=True,
    java_script_enabled=True,
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
               "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",)

context.add_init_script("""
  Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
  });
""")

page = context.new_page()

page.goto("https://www.lastminute.ae/")


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


home_page = HomePage(page)
home_page.close_cookies_message()
# home_page.click_flight_tab()
home_page.set_trip_direction()
home_page.set_passenger_type_and_count()
home_page.set_flight_class()
home_page.choose_outbound_flight("Dubai")
home_page.choose_inbound_flight("Riyadh")
home_page.set_flight_dates()
search_results_page = SearchResultsPage(page)
search_results_page.safe_load_search_results()
search_results_page.retry_search_with_alternative_dates()
search_results_page.check_elal_airline_filter()
flexi_page_object = search_results_page.choose_elal_flight()
flexi_page = FlexiPage(flexi_page_object)
flexi_page.wait_for_page_to_load()
flexi_page.choose_flexi_ticket()
contact_page = ContactPage(flexi_page_object)
contact_page.wait_for_contact_page_to_load()
contact_page.fill_contact_info(contact_first_name, contact_last_name, email, confirmation_email, phone_number)
contact_page.fill_passenger_info(passenger_first, passenger_last, birthday_date)
contact_page.add_outbound_baggage()
contact_page.add_inbound_baggage()
contact_page.continue_to_next_page_with_recovery(contact_first_name, contact_last_name, passenger_first, passenger_last, email, confirmation_email, phone_number, birthday_date)
ancillaries_page = AncillariesPage(flexi_page_object)
ancillaries_page.choose_ancillaries()
flight_summary_details = FlightSummaryDetails(flexi_page_object)
flight_summary_details.wait_for_summary_page_to_load()
flight_summary_details.verify_contact_details(contact_first_name, contact_last_name, phone_number, email)
flight_summary_details.verify_passenger_details(passenger_full_name, passenger_gender, birthday_date)
flight_summary_details.check_remark_quantity()
flight_summary_details.verify_general_services(
    "מזוודה לבטן המטוס",
    "כרטיס גמיש +",
    "חבילת שירות פרמיום מותאמת לעידן השינויים והביטולים",
    "להזמין בראש שקט",
    "מזוודה שאבדה יכולה להרוס נסיעה"
)
flight_summary_details.choose_credit_card_payments()
flight_summary_details.fill_credit_card_first_info("Natan", "Shor", "natan@lastminute.co.il", "0527491280")
flight_summary_details.verify_flight_price()
flight_summary_details.agree_and_pay()
flight_summary_details.fill_credit_card_details("5111565657768778", "345", "209596959")


