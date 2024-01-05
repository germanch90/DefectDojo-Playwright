import os
import pytest

from tests.pages import DefectDojoLoginPage

@pytest.fixture()
def login_page(page):
    """Setup the POM for login tests."""
    login_page_inst = DefectDojoLoginPage(page)
    # Let's navigate to the page before returning it.
    login_page_inst.navigate()
    return login_page_inst

@pytest.fixture()
def valid_password():
    pw = os.getenv('DD_TEST_PASSWORD')
    if not pw:
        raise ValueError("Environment variable for DD_TEST_PASSWORD is not set.")
