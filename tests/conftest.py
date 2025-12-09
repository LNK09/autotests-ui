import pytest
from playwright.sync_api import Page, Browser


@pytest.fixture(scope="session")
def initialize_browser_state(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    email_reg_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_reg_input.fill('user.name@gmail.com')

    username_reg_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_reg_input.fill('username')

    password_reg_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_reg_input.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    page.context.storage_state(path='browser-state.json')

    context.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, browser: Browser) -> Page:
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    context.close()
