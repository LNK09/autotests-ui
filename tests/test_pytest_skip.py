import pytest


@pytest.mark.skip(reason="Feature in dev")
def test_feature_in_development():
    ...


@pytest.mark.skip(reason="Features in dev")
class TestSuiteSkip:
    def test_feature_in_dev_1(self):
        ...

    def test_feature_in_dev_2(self):
        ...
