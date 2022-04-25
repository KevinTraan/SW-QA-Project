import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!'),
    balance=5000
)

# Mock a ticket
test_ticket = Ticket(
    owner = "test_frontend@test.com",
    name = "test_ticket",
    quantity = 10,
    price = 10,
    date = 20201230
)

class IndexTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    def _login(self, *_):
        # Navigate to /logout to invalidate any existing sessions
        self.open(base_url + '/logout')
        # Navigate to /login
        self.open(base_url + '/login')
        # Submit correct credentials
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click('input[type="submit"]')

    # 3.1 If the user hasn't logged in, redirect the login page
    def test_R3_1(self, *_):
        # Navigate to /logout to invalidate any existing sessions
        self.open(base_url + '/logout')
        # navigate to /login
        self.open(base_url + '/login')
        # verify login page is visible by checking expected elements
        self.assert_element("#email")
        self.assert_element("#password")
        self.assert_element("#btn-submit")
    
    # 3.2 This page shows a header 'Hi {}'.format(user.name)
    def test_R3_2(self, *_): 
        # Verify that profile page is visible by checking for `#welcome-header` element in DOM
        self._login()
        self.assert_element("#welcome-header")
        self.assert_text("Hi test_frontend", "#welcome-header")
    
    # 3.3 This page shows user balance.
    def test_R3_3(self, *_):
        self._login()
        # Verify that profile page shows user balance by checking for '#balance'
        self.assert_element("#balance")
        self.assert_text("User Balance: $5000", "#balance")
    
    
    # 3.4 This page shows a logout link, pointing to /logout
    def test_R3_4(self, *_):
        self._login()
        # Verify that profile page shows a logout link pointing to /logout
        self.assert_true(self.get_link_attribute('logout','href'), base_url+'/logout')

    # 3.5 This page lists all available tickets. Information including the quantity of each ticket,
    #the owner's email, and the price, for tickets that are not expired.
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    def test_R3_5(self, *_):
        self._login()
        # Verify that profile page shows all available tickets
        self.assert_element("#tickets div h4")
        self.assert_text(test_ticket.owner)
        self.assert_text(test_ticket.name)
        self.assert_text(test_ticket.quantity)
        self.assert_text(test_ticket.price)
        self.assert_text(test_ticket.date)
        
    # 3.6 This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date.
    def test_R3_6(self, *_):
        self._login()
        # Verify that profile page shows elements for sell form
        self.assert_element("#sell-name")
        self.assert_element("#sell-quantity")
        self.assert_element("#sell-price")
        self.assert_element("#sell-date")

    # 3.7 This page contains a form that a user can buy new tickets. Fields: name, quantity
    def test_R3_7(self, *_):
        self._login()
        # Verify that profile page shows elements for buy form
        self.assert_element("#buy-name")
        self.assert_element("#buy-quantity")

    # 3.8 This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date
    def test_R3_8(self, *_):
        self._login()
        # Verify that profile page shows elements for updating existing tickets
        self.assert_element("#update-name")
        self.assert_element("#update-quantity")
        self.assert_element("#update-price")
        self.assert_element("#update-date")

    # 3.9 The ticket-selling form can be posted to /sell.
    def test_R3_9(self, *_):
        self._login()
        # Verify that sell form can be posted to /sell
        self.type("#sell-name", test_ticket.owner)
        self.type("#sell-quantity", str(test_ticket.quantity))
        self.type("#sell-price", str(test_ticket.price))
        self.type("#sell-date", str(test_ticket.date))
        self.click('input[value="Sell"]')

    # 3.10 The ticket-buying form can be posted to /buy.
    def test_R3_10(self, *_):
        self._login()
        # Verify that buy form can be posted to /buy
        self.type("#buy-name", test_ticket.owner)
        self.type("#buy-quantity", str(test_ticket.quantity))
        self.click('input[value="Buy"]')

    # 3.11 The ticket-update form can be posted to /update.
    def test_R3_11(self, *_):
        self._login()
        # Verify that update form can be posted to /update
        self.type("#update-name", "updated_test_ticket")
        self.type("#update-quantity", str(11))
        self.type("#update-price", str(1))
        self.type("#update-date", str(20210101))
        self.click('input[value="Update"]')
