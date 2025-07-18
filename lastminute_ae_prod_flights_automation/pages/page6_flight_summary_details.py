from playwright.sync_api import Page
from automation.lastminute_automation.lastminute_ae_prod_flights_automation.pages.base_page import BasePage


class FlightSummaryDetails(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __CONTACT_FIRST_AND_LAST_NAME = ".details-item.top > .name > p"
    __CONTACT_PHONE_NUMBER = ".details-item.top > .phone > p"
    __CONTACT_EMAIL = ".details-item.top > .mail > p"
    __PASSENGER_FIRST_AND_LAST_NAME = ".details-container.pax  .details-item > .name"
    __PASSENGER_GENDER = ".details-container.pax  .details-item > .gender"
    __PASSENGER_BIRTHDAY = ".details-container.pax  .details-item > .dob"
    __SUMMARY_FLIGHT_DETAILS = '[key="Checkout.FlightDetailsSummary"]'
    __TRANSACTION_TERMS_BTN = ".tabs-container > div:nth-child(2)"
    __ORDER_SUMMARY_BTN = ".tabs-container > div:nth-child(1)"
    __TRANSACTION_TERMS_REMARKS_LIST = ".terms-container .term-item"
    __AGREEMENT_BTN = '.agreement-container > .checkbox > [type="checkbox"]'
    __PAY_BTN = ".payment-details-container .primary-btn"
    __FLEXIBLE_TICKET = "app-deal-summary-ancillaries app-deal-summary-row:nth-child(1)"
    __CACNELLATION_PACKAGE = "app-deal-summary-ancillaries app-deal-summary-row:nth-child(2)"
    __ANCILLAR_SERVICES_LIST = ".ancillries-container app-deal-summary-row .head"
    __ANCILLARY_SERVICES_TITLE = ".ancillries-container app-deal-summary-row .head > span:nth-child(1)"
    __ANCILLARIES = "app-deal-summary-ancillaries .head span:not(.quantity)"
    __NUMBER_OF_PAYMENTS_DROPDOWN = "app-payment-details app-number-of-payments .num-of-payments-container"
    __TWENTY_FOUR_PAYMENTS_OPTION = "app-number-of-payments .payments-pop-container .option-row:nth-child(9)"
    __SIX_PAYMENTS_OPTION = "app-number-of-payments .payments-pop-container .option-row:nth-child(6)"
    __ONE_PAYMENTS_OPTION = "app-number-of-payments .payments-pop-container .option-row:nth-child(1)"
    __PAYMENT_HOLDER_FIRST_NAME_FIELD = 'app-payment-details [name="fname"]'
    __PAYMENT_HOLDER_LAST_NAME_FIELD = 'app-payment-details [name="lname"]'
    __PAYMENT_HOLDER_EMAEIL_FIELD = 'app-payment-details [name="femail"]'
    __PAYMENT_HOLDER_PHONE_NUMBER_FIELD = 'app-payment-details [name="fphone"]'
    __FLIGHT_SUMMARY_PRICE = "app-checkout-summary  .value"
    __HEADER_STRIP_FLIGHT_PRICE = "app-checkout-header .price-value > span:nth-child(2)"
    __PAYMENT_SECTION_FLIGHT_PRICE = "app-number-of-payments .paymentPriceText"
    __CREDIT_CARD_IFRAME = "#iframeBox"
    __CREDIT_CARD_NUMBER_FIELD = "#cg-tx-container #card-number"
    __CREDIT_CARD_EXPIRED_YEAR_DROPDOWN = "#cg-tx-container #expYear"
    __CREDIT_CARD_EXPIRED_MONTH_DROPDOWN = "app-payment-form #expMonth"
    __CREDIT_CARD_CVV = "app-payment-form #cvv"
    __CREDIT_CARD_ID_HOLDER = "app-payment-form #personal-id"

    def wait_for_summary_page_to_load(self):
        self._page.wait_for_load_state("load")
        print("🌐 Current URL:", self._page.url)

        summary_element = self._page.locator(self.__SUMMARY_FLIGHT_DETAILS)
        summary_element.wait_for(state="visible", timeout=10000)

        assert summary_element.is_visible(), "❌ Flight summary details element not visible!"

        summary_text = summary_element.inner_text()
        print("📝 Flight summary details text found:")
        print(summary_text)

    def verify_contact_details(self, contact_first_name, contact_last_name, contact_phone, contact_email_address):
        self._page.wait_for_load_state("load")

        contact_full_name_element = self._page.locator(self.__CONTACT_FIRST_AND_LAST_NAME)
        contact_full_name_element.wait_for(state="visible", timeout=10000)
        actual_contact_full_name = contact_full_name_element.inner_text().strip()
        expected_contact_full_name = f"{contact_first_name} {contact_last_name}"
        assert expected_contact_full_name in actual_contact_full_name, \
            f"❌ Expected full name: '{expected_contact_full_name}', but got: '{actual_contact_full_name}'"
        print(f"✅ Contact full name matches: {actual_contact_full_name}")

        contact_phone_element = self._page.locator(self.__CONTACT_PHONE_NUMBER)
        contact_phone_element.wait_for(state="visible", timeout=10000)
        actual_contact_phone = contact_phone_element.inner_text().strip()
        expected_contact_phone = contact_phone
        assert expected_contact_phone in actual_contact_phone, \
            f"❌ Expected phone: '{expected_contact_phone}', but got: '{actual_contact_phone}'"
        print(f"✅ Contact phone number matches: {actual_contact_phone}")

        contact_email_element = self._page.locator(self.__CONTACT_EMAIL)
        contact_email_element.wait_for(state="visible", timeout=10000)
        actual_contact_email = contact_email_element.inner_text().strip()
        expected_contact_email = contact_email_address
        assert expected_contact_email in actual_contact_email, \
            f"❌ Expected email: '{expected_contact_email}', but got: '{actual_contact_email}'"
        print(f"✅ Contact email matches: {actual_contact_email}")

    def verify_passenger_details(self, passenger_full_name, passenger_gender, passenger_birthday):
        # Full Name
        full_name_element = self._page.locator(self.__PASSENGER_FIRST_AND_LAST_NAME)
        full_name_element.wait_for(state="visible", timeout=10000)
        actual_full_name = full_name_element.inner_text().strip()
        expected_full_name = passenger_full_name.strip()
        assert expected_full_name in actual_full_name, \
            f"❌ Expected full name: '{expected_full_name}', but got: '{actual_full_name}'"
        print(f"✅ Passenger full name matches: {actual_full_name}")

        # Gender
        gender_element = self._page.locator(self.__PASSENGER_GENDER)
        gender_element.wait_for(state="visible", timeout=10000)
        actual_gender = gender_element.inner_text().strip().replace('\u200f', '').replace('\u200e', '')
        expected_gender = passenger_gender.strip().replace('\u200f', '').replace('\u200e', '')
        assert expected_gender in actual_gender, \
            f"❌ Expected gender: '{expected_gender}', but got: '{actual_gender}'"
        print(f"✅ Passenger gender matches: {actual_gender}")

        # Birthday
        birthday_element = self._page.locator(self.__PASSENGER_BIRTHDAY)
        birthday_element.wait_for(state="visible", timeout=10000)
        actual_birthday = birthday_element.inner_text().strip().replace("/", "")
        expected_birthday = passenger_birthday.strip().replace("/", "")
        assert expected_birthday in actual_birthday, \
            f"❌ Expected birthday: '{expected_birthday}', but got: '{actual_birthday}'"
        print(f"✅ Passenger birthday matches: {actual_birthday}")

    def check_remark_quantity(self):
        # Click the "Transaction Terms" button
        transaction_terms_btn = self._page.locator(self.__TRANSACTION_TERMS_BTN)
        transaction_terms_btn.wait_for(state="visible", timeout=10000)
        assert transaction_terms_btn.is_visible(), "❌ 'Transaction Terms' button was not found!"
        self.click(transaction_terms_btn)
        print("✅ 'Transaction Terms' button was clicked.")

        # Wait for remarks to load
        self._page.wait_for_timeout(5000)
        self._page.wait_for_selector(self.__TRANSACTION_TERMS_REMARKS_LIST, timeout=30000)
        remark_area_list = self._page.locator(self.__TRANSACTION_TERMS_REMARKS_LIST)
        remark_count = remark_area_list.count()
        print(f"📝 {remark_count} remarks were found.")

        # Check at least 8 remarks exist
        assert remark_count >= 8, f"❌ Only {remark_count} remarks found. Expected at least 8."
        print("✅ Minimum of 8 remarks found.")

        # Click the "Order Summary" button
        order_summary_btn = self._page.locator(self.__ORDER_SUMMARY_BTN)
        order_summary_btn.wait_for(state="visible", timeout=10000)
        assert order_summary_btn.is_visible(), "❌ 'Order Summary' button was not found!"
        self.click(order_summary_btn)
        print("✅ 'Order Summary' button was clicked.")

    def verify_general_services(self, *expected_services: str):
        for service in expected_services:
            ancillaries = self._page.locator(self.__ANCILLARIES, has_text=service)
            assert ancillaries.is_visible(timeout=10000), f"❌ The service '{service}' was not found on the page!"
            print(f"✅ The service '{service}' was found successfully.")

    def choose_credit_card_payments(self):
        payment_options = [
            self.__TWENTY_FOUR_PAYMENTS_OPTION,
            self.__SIX_PAYMENTS_OPTION,
            self.__ONE_PAYMENTS_OPTION
        ]

        for option in payment_options:
            payments_dropdown = self._page.locator(self.__NUMBER_OF_PAYMENTS_DROPDOWN)
            payments_dropdown.wait_for(state="visible", timeout=10000)
            assert payments_dropdown.is_visible(), "❌ Payments number dropdown was not found!"
            self.click(payments_dropdown)
            print("✅ Payments number dropdown was clicked.")

            selected_option = self._page.locator(option)
            selected_option.wait_for(state="visible", timeout=10000)
            assert selected_option.is_visible(), f"❌ Payment option '{option}' was not found!"
            self.click(selected_option)
            print(f"✅ Payment option '{option}' was selected.")

    def fill_credit_card_first_info(self, first_name, last_name, email_address, phone_number):
        # First name
        first_name_field = self._page.locator(self.__PAYMENT_HOLDER_FIRST_NAME_FIELD)
        first_name_field.wait_for(state="visible", timeout=10000)
        assert first_name_field.is_visible(), "❌ First name field was not found!"
        self.fill_info(first_name_field, first_name)
        print("✅ First name was filled successfully.")

        # Last name
        last_name_field = self._page.locator(self.__PAYMENT_HOLDER_LAST_NAME_FIELD)
        last_name_field.wait_for(state="visible", timeout=10000)
        assert last_name_field.is_visible(), "❌ Last name field was not found!"
        self.fill_info(last_name_field, last_name)
        print("✅ Last name was filled successfully.")

        # Email address
        email_address_field = self._page.locator(self.__PAYMENT_HOLDER_EMAEIL_FIELD)
        email_address_field.wait_for(state="visible", timeout=10000)
        assert email_address_field.is_visible(), "❌ Email address field was not found!"
        self.fill_info(email_address_field, email_address)
        print("✅ Email address was filled successfully.")

        # Phone number
        phone_number_field = self._page.locator(self.__PAYMENT_HOLDER_PHONE_NUMBER_FIELD)
        phone_number_field.wait_for(state="visible", timeout=10000)
        assert phone_number_field.is_visible(), "❌ Phone number field was not found!"
        self.fill_info(phone_number_field, phone_number)
        print("✅ Phone number was filled successfully.")

    def verify_flight_price(self):
        # Summary section price
        flight_summary_price = self._page.locator(self.__FLIGHT_SUMMARY_PRICE)
        flight_summary_price.wait_for(state="visible", timeout=10000)
        flight_summary_price_text = flight_summary_price.inner_text().strip()
        print(f"🧾 Flight summary section price: {flight_summary_price_text}")

        # Header strip price
        header_strip_flight_price = self._page.locator(self.__HEADER_STRIP_FLIGHT_PRICE)
        header_strip_flight_price.wait_for(state="visible", timeout=10000)
        header_strip_flight_price_text = header_strip_flight_price.inner_text().strip()
        print(f"📌 Header strip price: {header_strip_flight_price_text}")

        # Payment section price
        payment_section_flight_price = self._page.locator(self.__PAYMENT_SECTION_FLIGHT_PRICE)
        payment_section_flight_price.wait_for(state="visible", timeout=10000)
        payment_section_flight_price_text = payment_section_flight_price.inner_text().replace("$", "").strip()
        print(f"💳 Payment section price: {payment_section_flight_price_text}")

        # Assertion
        assert (
                flight_summary_price_text == header_strip_flight_price_text == payment_section_flight_price_text
        ), (
            f"❌ Price mismatch detected!\n"
            f"  ➤ Summary: {flight_summary_price_text}\n"
            f"  ➤ Header: {header_strip_flight_price_text}\n"
            f"  ➤ Payment: {payment_section_flight_price_text}"
        )

        print("✅ All flight prices match successfully!")

    def agree_and_pay(self):
        self._page.wait_for_timeout(3000)

        # Click agreement checkbox
        agreement_checkbox = self._page.locator(self.__AGREEMENT_BTN)
        agreement_checkbox.wait_for(state="visible", timeout=10000)
        assert agreement_checkbox.is_visible(), "❌ Agreement checkbox was not found on the page!"
        self.click(agreement_checkbox)
        print("✅ Agreement checkbox was clicked.")

        # Click pay button
        pay_button = self._page.locator(self.__PAY_BTN)
        pay_button.wait_for(state="visible", timeout=10000)
        assert pay_button.is_visible(), "❌ Pay button was not found on the page!"
        self.click(pay_button)
        print("💳 Pay button was clicked. Payment process initiated.")

    def fill_credit_card_details(self, credit_card_number, credit_card_cvv, credit_card_id_holder):

        self._page.wait_for_load_state("load")
        frame = self._page.frame_locator(self.__CREDIT_CARD_IFRAME)


        # 1. מספר כרטיס אשראי
        credit_card_number_field = frame.locator(self.__CREDIT_CARD_NUMBER_FIELD)
        credit_card_number_field.wait_for(state="visible", timeout=50000)
        assert credit_card_number_field.is_visible(), "❌ Credit card number field is not visible"
        self.fill_info(credit_card_number_field, credit_card_number)
        print("✅ Credit card number was entered successfully!")

        # 2. שנה
        year_expiration_card_dropdown = frame.locator(self.__CREDIT_CARD_EXPIRED_YEAR_DROPDOWN)
        year_expiration_card_dropdown.wait_for(state="visible", timeout=30000)
        assert year_expiration_card_dropdown.is_visible(), "❌ Year dropdown not visible"
        year_expiration_card_dropdown.select_option("40")
        print("✅ Selected year 2040!")

        # 3. חודש
        month_expiration_card_dropdown = frame.locator(self.__CREDIT_CARD_EXPIRED_MONTH_DROPDOWN)
        month_expiration_card_dropdown.wait_for(state="visible", timeout=30000)
        assert month_expiration_card_dropdown.is_visible(), "❌ Month dropdown not visible"
        month_expiration_card_dropdown.select_option("10")
        print("✅ Selected month 10 (October)!")

        # 4. CVV
        credit_card_cvv_field = frame.locator(self.__CREDIT_CARD_CVV)
        credit_card_cvv_field.wait_for(state="visible", timeout=30000)
        assert credit_card_cvv_field.is_visible(), "❌ CVV field not visible"
        self.fill_info(credit_card_cvv_field, credit_card_cvv)
        print("✅ The CVV field was filled!")

        # 5. ת.ז. בעל הכרטיס
        credit_card_id_holder_field = frame.locator(self.__CREDIT_CARD_ID_HOLDER)
        credit_card_id_holder_field.wait_for(state="visible", timeout=30000)
        assert credit_card_id_holder_field.is_visible(), "❌ Credit card ID holder field not visible"
        self.fill_info(credit_card_id_holder_field, credit_card_id_holder)
        print("✅ The credit card holder ID was filled successfully!")





















