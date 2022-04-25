import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import Mock, patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!'),
    balance=0
)

class FrontEndLoginTest(BaseCase):

    # R1.1 If the user hasn't logged in, show the login page.
    # R1.2 The login page has a message that by default says 'please login'.
    # R1.4 The login page provides a login form which requests two fields: email and password.
    def test_login_page(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

    # R1.3 If the user has logged in, redirect to the user profile page.
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    def test_login_redirect(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # navigate to login page again
        self.open(base_url + '/login')
        # verify redirect occurred
        self.assert_element_present("h2#welcome-header")
        self.assert_text("Hi", "h2#welcome-header")

    # R1.5 The login form can be submitted as a POST request to the current URL.
    # R1.7a Valid email can login.
    # R1.10 If email/password are correct, redirect to `/`
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    def test_login_valid_credentials(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # verify `/` page is displayed
        self.assert_element_present("h2#welcome-header")
        self.assert_text("Hi", "h2#welcome-header")

    # R1.6a Empty email and password does not login.
    def test_login_empty_inputs(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit empty form
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

    # R1.6b Empty email does not login.
    def test_login_empty_password(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit incomplete form
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

    # R1.6c Empty password does not login.
    def test_login_empty_email(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit incomplete form
        self.type("#email", test_user.email)
        self.click("input#btn-submit")
        # verify all form elements present
        self.assert_element_present("h1")
        self.assert_text("Log In", "h1")
        self.assert_element_present("h4#message")
        self.assert_text("Please login", "h4#message")
        self.assert_element_present("input#email")
        self.assert_element_present("input#password")
        self.assert_element_present("input#btn-submit")

    # R1.7b Invalid email cannot login and error message 'email/password format is incorrect' is displayed.
    def test_login_invalid_email_format(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", "test_frontend")
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password format is incorrect", "h4#message")

    # R1.8a User with password shorter than 6 characters cannot log in
    # and error message 'email/password format is incorrect' is displayed.
    def test_login_invalid_password_less_than_6_characters(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", "Pass!")
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password format is incorrect", "h4#message")

    # R1.8b User with password with no uppercase characters cannot log in
    # and error message 'email/password format is incorrect' is displayed.
    def test_login_invalid_password_no_uppercase(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", "password!")
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password format is incorrect", "h4#message")

    # R1.8c User with password with no lowercase characters cannot log in
    # and error message 'email/password format is incorrect' is displayed.
    def test_login_invalid_password_no_lowercase(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", "PASSWORD!")
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password format is incorrect", "h4#message")

    # R1.8d User with password with no special characters cannot log in
    # and error message 'email/password format is incorrect' is displayed.
    def test_login_invalid_password_no_lowercase(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", "Password")
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password format is incorrect", "h4#message")

    # R1.11a Invalid email redirects to `/login` with error message.
    @patch('qa327.backend.login_user', return_value=None)
    def test_login_invalid_email_credential(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", "testing@test.com")
        self.type("#password", test_user.password)
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password combination incorrect", "h4#message")

    # R1.11b Invalid password redirects to `/login` with error message.
    @patch('qa327.backend.login_user', return_value=None)
    def test_login_invalid_password_credential(self, *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # navigate to login page
        self.open(base_url + '/login')
        # submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", "WrongPassword!")
        self.click("input#btn-submit")
        # verify error message
        self.assert_element_present("h4#message")
        self.assert_text("email/password combination incorrect", "h4#message")