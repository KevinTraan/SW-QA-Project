import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.models import db, User, Ticket
import qa327.backend as bn


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).
test_user = User(
    email='test_frontend@test.com',
    name='test frontend',
    password='Password!',
    balance=5000
)
test_ticket = Ticket(
    owner = 'test_frontend@test.com',
    name = 'test ticket',
    quantity = "1",
    price = "20",
    date = "20210901"
)

@pytest.mark.usefixtures('server')
class Integration(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click('input[type="submit"]')

    def sell(self):
        # create a ticket to sell
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_not_visible("#message")
        self.assert_element_visible("#tickets")
        self.assert_text_visible(test_ticket.name, "#tickets")

    def test_register_login(self):
        """ This test checks the implemented login/logout feature """
        bn.delete_database()
        self.register()
        self.login()
        self.open(base_url)
        self.assert_element_present("#welcome-header")
        self.assert_text("Hi " + test_user.name, "#welcome-header")
        # cleanup after test by removing registered user

    def test_sell(self):
        bn.delete_database()
        # register new user and login
        self.register()
        self.login()
        self.open(base_url)
        self.sell()

    def test_buy(self):
        # register new user, login, and create ticket to buy
        bn.delete_database()
        self.register()
        self.login()
        self.open(base_url)
        self.sell()
        # buy the created ticket
        self.type("#buy-name", test_ticket.name)
        self.type("#buy-quantity", test_ticket.quantity)
        self.click("input.buy")
        self.assert_element_not_visible("#message")
        self.assert_text_not_visible(test_ticket.name, "#tickets")
        balance = bn.get_balance(test_user.email)
        self.assertLess(balance, test_user.balance, "error with buying ticket - balance did not change")
