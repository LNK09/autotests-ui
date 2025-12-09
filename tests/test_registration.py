from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_reg_input = chromium_page.get_by_test_id('registration-form-email-input').locator('//div//input')
    email_reg_input.fill('user.name@gmail.com')

    username_reg_input = chromium_page.get_by_test_id('registration-form-username-input').locator('//div//input')
    username_reg_input.fill('username')

    password_reg_input = chromium_page.get_by_test_id('registration-form-password-input').locator('//div//input')
    password_reg_input.fill('password')

    reg_button = chromium_page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')
