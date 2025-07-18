import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--start-maximized",
            "--disable-web-security",
            "--allow-running-insecure-content",
            "--disable-features=IsolateOrigins,SitePerProcess,SameSiteByDefaultCookies,BlockThirdPartyCookies",
            "--disable-blink-features=AutomationControlled"
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
    page.goto("https://www.lastminute.co.il/")
    yield page
    context.close()
