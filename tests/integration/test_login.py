from playwright.sync_api import Page, expect
import re

from tests.pages.defect_dojo_page import DefectDojoLoginPage

class TestLogin:

    def test_valid_login(self, login_page: DefectDojoLoginPage, valid_password: str):
        """Test that a valid login succeeds."""
        login_page.login(username='admin', password=valid_password)

        # Check that login succeded and we are redirected to the dashboard
        expect(login_page.page).to_have_url(re.compile(r".*/dashboard"))


    def test_invalid_login(self, login_page: DefectDojoLoginPage):
        """Test that an invalid login fails."""
        # Let's first make sure Invalid Login message is not there.
        expect(login_page.invalid_login_message).not_to_be_attached()

        # Fill in the form with invlaid credentials.
        login_page.login(username='admin', password='not_valid_pass')

        # Let's check the error message is displayed and contains the correct wording.
        # Remember the banner goes away after a couple of seconds.
        expect(login_page.invalid_login_message).to_be_attached()
        expect(login_page.invalid_login_message).to_contain_text('Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def test_username_is_mandatory(self, login_page:DefectDojoLoginPage):
        """Test that login errors if username is not given."""
        # We are providing an empty value for username.
        login_page.login(username='', password='invalid')
        # User is retained in the login page.
        expect(login_page.page).to_have_url(re.compile(r'.*/login'))

    def test_password_is_mandatory(self, login_page:DefectDojoLoginPage):
        """Test that login errors if password is not given."""
        # We are providing an empty value for password.
        login_page.login(username='admin', password='')
        # User is retained in the login page.
        expect(login_page.page).to_have_url(re.compile(r'.*/login'))