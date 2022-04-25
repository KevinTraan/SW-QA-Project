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

class OtherTest(BaseCase):

    def test_R8_1a(self, *_):
        """
        When not logged in return a 404 error for any other requests except the authorized ones
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /badrequest
        self.open(base_url + '/badrequest')
        # Verify current page displays 404 error message by checking title
        self.assert_title("404 Not Found")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R8_1b(self, *_):
        """
        When logged in return a 404 error for any other requests except the authorized ones
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Enter `test_user.email` in `#email` element
        self.type("#email", test_user_unhashed.email)
        # Enter `test_user.password` in `#password` element
        self.type("#password", test_user_unhashed.password)
        # Click on `#btn-submit` element
        self.click('input[type="submit"]')
        # Navigate to /badrequest
        self.open(base_url + '/badrequest')
        # Verify current page displays 404 error message by checking title
        self.assert_title("404 Not Found")

    def test_R8_1c(self, *_):
        """
        When not logged in ensure a 404 error is not sent for the authorized requests
        """
        # Navigate to /logout (Invalidate any logged-in sessions)
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Verify current page does not display the 404 error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R8_1d(self, *_):
        """
        When logged in ensure a 404 error is not sent for the authorized requests
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
        # Navigate to /
        self.open(base_url + '/')
        # Verify current page does not display the 404 error message by checking content of `#welcome-header`
        self.assert_element("#welcome-header")
        self.assert_text("Hi test_frontend", "#welcome-header")