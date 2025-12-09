import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] - sending data in analytics service")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] - initialize settings for autotests")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] - creating user data one time for testing class")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] - open browser on every autotest")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...
