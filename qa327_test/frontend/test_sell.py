import pytest, time
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import Mock, patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password!',
    balance=5000
)
# Mock some sample tickets
test_ticket = Ticket(
    owner = 'test_frontend@test.com',
    name = 'test ticket',
    quantity = "1",
    price = "20",
    date = "20210901"
)


class SellTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    def login(self,  *_):
        # invalidate all sessions
        self.open(base_url + '/logout')
        # login to access profile page
        self.open(base_url + '/login')
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        self.click("input#btn-submit")


    # R4.1a Ticket name with special characters produces an error message.
    def test_R4_1a(self, *_):
        self.login(self)
        self.type("#sell-name", "test ticker!@#")
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("ticket name format is incorrect", "h4#message")

    # R4.1b Ticket name with leading space produces an error message.
    def test_R4_1b(self, *_):
        self.login(self)
        self.type("#sell-name", " leading space")
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("ticket name format is incorrect", "h4#message")

    # R4.1c Ticket name with trailing space produces an error message.
    def test_R4_1c(self, *_):
        self.login(self)
        self.type("#sell-name", "trailing space ")
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("ticket name format is incorrect", "h4#message")

    # R4.2 Ticket name longer than 60 characters produces an error message.
    def test_R4_2(self, *_):
        self.login(self)
        self.type("#sell-name", "0123456789012345678901234567890123456789012345678901234567890")
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("ticket name format is incorrect", "h4#message")

    # R4.3a Ticket quantity of 0 or less produces an error message.
    def test_R4_3a(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", "0")
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("quantity format is incorrect", "h4#message")

    # R4.3b Ticket quantity of over 100 produces an error message.
    def test_R4_3b(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", "200")
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("quantity format is incorrect", "h4#message")

    # R4.4a Price of less than 10 produces an error message.
    def test_R4_4a(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", "5")
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("price format is incorrect", "h4#message")

    # R4.4b Price of greater than 100 produces an error message.
    def test_R4_4b(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", "200")
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("price format is incorrect", "h4#message")

    # R4.5a Mis-formatted date produces error message.
    def test_R4_5a(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", "2020-12-12")
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("date format is incorrect", "h4#message")

    # R4.5b Date in the past produces error message.
    def test_R4_5b(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", "20200101")
        self.click("input.sell")
        self.assert_element_present("h4#message")
        self.assert_text("date format is incorrect", "h4#message")

    # R4.7 The added new ticket information will be posted on the user profile page.
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.set_ticket', return_value=None)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    def test_R4_7(self, *_):
        self.login(self)
        self.type("#sell-name", test_ticket.name)
        self.type("#sell-quantity", test_ticket.quantity)
        self.type("#sell-price", test_ticket.price)
        self.type("#sell-date", test_ticket.date)
        self.click("input.sell")
        self.assert_element_not_visible("#message")
        self.assert_element("#tickets")





