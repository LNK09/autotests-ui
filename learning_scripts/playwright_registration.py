from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_reg_input = page.get_by_test_id('registration-form-email-input').locator('//div//input')
    email_reg_input.fill('user.name@gmail.com')

    username_reg_input = page.get_by_test_id('registration-form-username-input').locator('//div//input')
    username_reg_input.fill('username')

    password_reg_input = page.get_by_test_id('registration-form-password-input').locator('//div//input')
    password_reg_input.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    context.storage_state(path='../browser-state.json')

    # expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_be_visible()
    # expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_have_text('Dashboard')
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
