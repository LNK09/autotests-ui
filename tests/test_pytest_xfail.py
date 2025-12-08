import pytest


@pytest.mark.xfail(
    reason="Bug link https://url.com"
)
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail
def test_without_bug():
    ...


