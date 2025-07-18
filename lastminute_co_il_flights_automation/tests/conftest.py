import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--start-maximized",  # לפתוח במסך מלא
            "--disable-web-security",  # לבטל מגבלות אבטחה (למניעת חסימות)
            "--allow-running-insecure-content",  # לאפשר תוכן לא מאובטח
            "--disable-features=IsolateOrigins,...",  # לבטל פיצ'רים שמקשים על אוטומציה
            "--disable-blink-features=AutomationControlled"  # להסוות שאנחנו בוט
        ],
        ignore_default_args=["--enable-automation"]
    )

    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True)
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined });")
    page = context.new_page()
    yield page
    context.close()
