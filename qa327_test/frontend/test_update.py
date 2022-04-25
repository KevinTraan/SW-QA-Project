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
    balance=0
)

# Sample user with an unhashed password
test_user_unhashed = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password!',
)

# Mock some sample tickets, all attributes are strings due to error with Github's pytest
test_ticket = Ticket(
    owner = 'test_frontend@test.com',
    name = 'Test Ticket',
    quantity = '1',
    price = '20',
    date = '20210901'
)

class UpdateTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_1a(self, *_):
        """
        The name of the ticket must be alphanumeric-only.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter “#invalidticket” into `#update_name` element
        self.type("#update-name", "#invalidticket")
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity)
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date)
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_1b(self, *_):
        """
        The name of the ticket is not allowed if the first character is a space.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter “ firstchar” into `#update_name` element
        self.type("#update-name", " firstchar")
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_1c(self, *_):
        """
        The name of the ticket is not allowed if the last character is a space.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter “lastchar ” into `#update_name` element
        self.type("#update-name", "lastchar ")
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

            
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_2(self, *_):
        """
        The name of the ticket is no longer than 60 characters
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter “unfortunatelythistickethasalittleoversixtycharactersinitsname” into `#update_name` element
        self.type("#update-name", "unfortunatelythistickethasalittleoversixtycharactersinitsname")
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket name is incorrect", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')
 

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_3a(self, *_):
        """
        The quantity of the tickets has to be more than 0.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name) 
        # Enter “0” into `#update_quantity` element
        self.type("#update-quantity", "0") 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid quantity in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_3b(self, *_):
        """
        The quantity of the tickets has to be less than or equal to 100.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter “101” into `#update_quantity` element 
        self.type("#update-quantity", "101") 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid quantity in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_4a(self, *_):
        """
         Price has to be greater than or equal to 10.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter “9” into `#update_price` element
        self.type("#update-price", "9")
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid price in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_4b(self, *_):
        """
         Price has to be less than or equal to 100.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter “101” into `#update_price` element
        self.type("#update-price", "101")
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid price in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_5a(self, *_):
        """
        Year must be formatted properly.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter “170901” into `#update_date` element
        self.type("#update-date", "170901") 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid date in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_5b(self, *_):
        """
        Month must be formatted properly.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter “20202001” into `#update_date` element
        self.type("#update-date", "20202001") 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid date in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_5c(self, *_):
        """
        Day must be formatted properly.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter “20201232” into `#update_date` element 
        self.type("#update-date", "20201232") 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid date in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_5d(self, *_):
        """
        Date must not have passed.
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter “19870101” into `#update_date` element 
        self.type("#update-date", "19870101")
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Invalid date in ticket update form", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_6(self, *_):
        """
        The ticket of the given name must exist
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter “anonexistentticket” into `#update_name` element
        self.type("#update-name", "anonexistentticket")  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `test_ticket.price` into `#update_price` element 
        self.type("#update-price", test_ticket.price)
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays error message by checking content of `#message`
        self.assert_element("#message")
        self.assert_text("Ticket does not exist", "#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.update_ticket', return_value=None)
    def test_R5_7b(self, *_):
        """
        An update without errors passes successfully
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
        # Navigate to /
        self.open(base_url + '/')
        # Enter `test_ticket.name` into `#update_name` element
        self.type("#update-name", test_ticket.name)  
        # Enter `test_ticket.quantity` into `#update_quantity` element  
        self.type("#update-quantity", test_ticket.quantity) 
        # Enter `22` into `#update_price` element
        self.type("#update-price", "22")
        # Enter `test_ticket.date` into `#update_date` element 
        self.type("#update-date", test_ticket.date) 
        # Click on `#update-submit` element
        self.click('input[value="Update"]')
        # Verify profile page displays no error
        self.assert_element_not_visible("#message")
        # Navigate to /logout (clean up)
        self.open(base_url + '/logout')