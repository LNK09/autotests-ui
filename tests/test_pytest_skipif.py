import pytest

SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="Test cant be started on version 1.3.0"
)
def test_sys_version_valid():
    ...


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="Test cant be started on version 1.2.0"
)
def test_sys_version_invalid():
    ...
