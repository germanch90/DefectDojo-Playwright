from playwright.sync_api import Page

base_url = 'https://demo.defectdojo.org/'

class DefectDojoPage:
    """Page model for the base DefectDojo application."""

    def __init__(self, page: Page):
        """Constructor method for base page model."""
        # Page attribute used to interface to Playwright page object
        self.page = page
        self.base_url = base_url
    
    def navigate(self, path: str):
        """Navigate to the given path by concatenating the base url and provided path."""
        self.page.goto(self.base_url + path)

class DefectDojoLoginPage(DefectDojoPage):
    """Page model for the Login Page"""

    def __init__(self, page: Page):
        """Constructor method for login page"""
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role('button', name='Login')
        self.invalid_login_message = page.get_by_text("Please enter a correct")

    def navigate(self):
        """Navigate to the login path."""
        path = '/login'
        return super().navigate(path)
    
    def enter_username(self, username: str):
        """Fill the username form field with the provided username value."""
        # As a best practice, let's ensure the field is blank.
        self.username_input.clear()
        self.username_input.fill(username)

    def enter_password(self, password: str):
        """Fill the password form field with the provided password value."""
        # As a best practice, let's ensure the field is blank.
        self.password_input.clear()
        self.password_input.fill(password)

    def login(self, username: str, password: str):
        """Fill the login form fields and click on the login button."""
        self.enter_username(username)
        self.enter_password(password)
        self.login_button.click()
    
