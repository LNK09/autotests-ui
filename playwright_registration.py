from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_reg_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
    email_reg_input.fill('user.name@gmail.com')

    username_registration_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
    username_registration_input.fill('username')

    password_registration_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
    password_registration_input.fill('password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()

    expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_be_visible()
