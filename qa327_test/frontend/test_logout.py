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

class LogoutTest(BaseCase):

    def test_R7_1a(self, *_):
        """
        Basic logout invalidates the current session check
        """
        # Navigate to /logout
        self.open(base_url + '/logout')
        # Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM
        self.assert_title("Log In")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R7_1b(self, *_):
        """
        Advanced logout invalidates the current session check
        """
        # Navigate to /logout
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Enter `test_user.email` in `#email` element
        self.type("#email", test_user_unhashed.email)
        # Enter `test_user.password` in `#password` element
        self.type("#password", test_user_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Navigate to /logout
        self.open(base_url + '/logout')
        # Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM
        self.assert_title("Log In")

    def test_R7_1c(self, *_):
        """
        After logout user can’t access restricted pages
        """
        # Navigate to /logout
        self.open(base_url + '/logout')
        # Navigate to /
        self.open(base_url + '/')
        # Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM
        self.assert_title("Log In")