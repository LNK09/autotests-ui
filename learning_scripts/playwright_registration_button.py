from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    email_registration_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_registration_input.fill('user.name@gmail.com')

    username_registration_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_registration_input.focus()
    expect(username_registration_input).to_be_focused()
    page.keyboard.type('username')

    password_registration_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_registration_input.focus()
    expect(password_registration_input).to_be_focused()
    for char in 'password':
        page.keyboard.press(char)

    expect(registration_button).to_be_enabled()
