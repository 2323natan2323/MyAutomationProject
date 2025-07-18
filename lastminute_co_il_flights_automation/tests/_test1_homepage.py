import pytest
from playwright.sync_api import sync_playwright
from automation.lastminute_automation.utils.config import ConfigReader
from automation.lastminute_automation.lastminute_co_il_flights_automation.pages.page1_home_page import HomePage


def test_co_il_flights_test1_homepage_test():

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

    browser.close()
