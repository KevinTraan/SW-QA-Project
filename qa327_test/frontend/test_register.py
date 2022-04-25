import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!'),
    balance=0
)

# Sample user with an unhashed password
test_user_unhashed = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password!',
)

# Mock a newly registered sample user
test_valid = User(
    email='valid.email@address.com',
    name='Valid Username',
    password=generate_password_hash('ValidP@ssword'),
    balance=5000
)

# Newly registered sample user with an unhashed password
test_valid_unhashed = User(
    email='valid.email@address.com',
    name='Valid Username',
    password='ValidP@ssword',
)

class RegisterTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R2_1(self, *_):
        """
        If the user has logged in, redirect back to the user profile page
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Enter `test_user_unhashed.email` in `#email` element
        self.type("#email", test_user_unhashed.email)
        # Enter `test_user_unhashed.password` in `#password` element
        self.type("#password", test_user_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Navigate to /register
        self.open(base_url + '/register')
        # Verify that profile page is visible by checking for `#welcome-header` element in DOM
        self.assert_element("#welcome-header")
        self.assert_text("Hi test_frontend", "#welcome-header")

    def test_R2_2(self, *_):
        """
        Otherwise, show the user registration page
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Verify that register page is visible by checking for expected elements (eg. `form-group`) in DOM
        self.assert_title("Register")


    def test_R2_3(self, *_):
        """
        The registration page shows a registration form requesting: 
        email, user name, password, password2
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Verify that `#email`, `#name`, `#password`, and `#password2` elements exist in the DOM
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")

    @patch('qa327.backend.register_user', return_value=None)
    def test_R2_4(self, *_):
        """
        The registration form can be submitted as a POST request to the current URL (/register)
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM
        self.assert_title("Log In")

    def test_R2_5a(self, *_):
        """
        Email cannot be empty
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")

    def test_R2_5b(self, *_):
        """
        Password cannot be empty
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")

    def test_R2_5c(self, *_):
        """
        Password2 cannot be empty
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")
        

    def test_R2_5d(self, *_):
        """
        Email has to follow addr-spec defined in RFC 5322 
        (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation)
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter “not.@.valid@email_address.com” in `#email` element
        self.type("#email", "not.@.valid@email_address.com")
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")

    def test_R2_5e(self, *_):
        """
        Password has to meet the required complexity: minimum length 6
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter “$Mall” in `#password` element
        self.type("#password", "$Mall")
        # Enter “$Mall” in `#password2` element
        self.type("#password2", "$Mall")
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")

    def test_R2_5f(self, *_):
        """
        Password has to meet the required complexity: at least one upper case
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter “lowerc@se” in `#password` element
        self.type("#password", "lowerc@se")
        # Enter “lowerc@se” in `#password2` element
        self.type("#password2", "lowerc@se")
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")

    def test_R2_5g(self, *_):
        """
        Password has to meet the required complexity: least one lower case
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter “UPPERC@SE” in `#password` element
        self.type("#password", "UPPERC@SE")
        # Enter “UPPERC@SE” in `#password2` element
        self.type("#password2", "UPPERC@SE")
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")


    def test_R2_5h(self, *_):
        """
        Password has to meet the required complexity: at least one special character
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter “noSpecial” in `#password` element
        self.type("#password", "noSpecial")
        # Enter “noSpecial” in `#password2` element
        self.type("#password2", "noSpecial")
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Email/Password combination incorrect", "#message")

    def test_R2_6(self, *_):
        """
        Password and password2 have to be exactly the same
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a different valid password (e.g. “AlsoValidP@ssword”) in `#password2` element
        self.type("#password2", "AlsoValidP@ssword")
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_R2_7a(self, *_):
        """
        Username has to be non-empty.
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Username format error", "#message")

    def test_R2_7b(self, *_):
        """
        Username has to be alphanumeric-only.
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter “#alphanumer” in `#name` element
        self.type("#name", "#alphanumer")
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Username format error", "#message")

    def test_R2_8a(self, *_):
        """
        Username has to be longer than 2 characters.
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter “2C” in `#name` element
        self.type("#name", "2C")
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Username format error", "#message")

    def test_R2_8b(self, *_):
        """
        Username has to be less than 20 characters.
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter “twentycharacterslong” `#name` element
        self.type("#name", "twentycharacterslong")
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Username format error", "#message")

    @patch('qa327.backend.register_user', return_value="This email has been ALREADY used")
    def test_R2_10(self, *_):
        """
        If the email already exists, show message 'This email has been ALREADY used'
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("This email has been ALREADY used", "#message")

    @patch('qa327.backend.get_user', return_value=test_valid)
    @patch('qa327.backend.register_user', return_value=None)
    def test_R2_11(self, *_):
        """
        If no error regarding the inputs following the rules above, 
        create a new user, set the balance to 5000, and go back to the /login page
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Navigate to /register
        self.open(base_url + '/register')
        # Enter a valid username (e.g. “Valid Username”) in `#name` element
        self.type("#name", test_valid_unhashed.name)
        # Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
        self.type("#password2", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Enter the same valid email address (e.g. “valid.email@address.com”) in `#email` element
        self.type("#email", test_valid_unhashed.email)
        # Enter the same valid password (e.g. “ValidP@ssword”) in `#password` element
        self.type("#password", test_valid_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Verify current page displays balance at 5000 by checking content of `#balance_message`
        self.assert_element("#balance")
        self.assert_text("User Balance: $5000", "#balance")