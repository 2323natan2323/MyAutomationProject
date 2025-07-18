import pytest
from playwright.sync_api import sync_playwright

from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page1_home_page import HomePage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page2_search_results_page import \
    SearchResultsPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page3_flexi_page import FlexiPage
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page4_contact_page import ContactPage



def test_co_il_flight_homepage_to_step3_contact_page():

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

    page.goto("https://www.lastminute.co.il/")


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
    home_page.click_flight_tab()
    home_page.set_trip_direction()
    home_page.set_passenger_type_and_count()
    home_page.set_flight_class()
    home_page.choose_outbound_flight("תל אביב")
    home_page.choose_inbound_flight("אתונה")
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