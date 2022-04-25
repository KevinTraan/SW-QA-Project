from flask import render_template, request, session, redirect
from qa327 import app
from datetime import date
import qa327.backend as bn
import re

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
def register_get():
    # if already logged in, redirect to profile page
    if 'logged_in' in session:
        return redirect('/')
    else:
        # templates are stored in the templates folder
        return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if (email_check(email) is None) or (pwd_check(password) is None):  # no match in regex
        error_message = 'Email/Password combination incorrect'

    elif password != password2:
        error_message = "The passwords do not match"

    elif username_check(name) is None:  # no match in regex
        error_message = "Username format error"

    else:
        error_message = bn.register_user(email, name, password, password2)

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('login.html', message=error_message)
    else:
        return redirect('/login')


def username_check(name):
    if name != None:
        # regex to check username is alphanumeric
        regex = '^[a-zA-Z0-9]+[a-zA-Z0-9 ]?[a-zA-Z0-9]+$'
        # check username is of required length
        if len(name) > 2 and len(name) < 20:
            return re.match(regex, name)


@app.route('/login', methods=['GET'])
def login_get():
    if 'logged_in' in session:
        return redirect('/')
    else:
        return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    if (email_check(email) is None) or (pwd_check(password) is None):  # no match in regex
        return render_template('login.html', message='email/password format is incorrect')

    else:
        user = bn.login_user(email, password)

    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='email/password combination incorrect')


def email_check(email):
    if email != None:
        # regex to check email conforms to RFC-5322
        regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        return re.match(regex, email)


def pwd_check(password):
    if password != None:
        # regex to check pwd conforms to minimum length 6,
        # at least an upper case, a lower case, and a special characters
        regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\W)[A-Za-z\d\W]{6,}$'
        return re.match(regex, password)


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)


@app.route('/', methods=['POST'])
def form_button():
    if "Update" in request.form['submit']:
        error_message = update_post()
    elif "Buy" in request.form['submit']:
        error_message = buy_post()
    elif "Sell" in request.form['submit']:
        error_message = sell_post()
    # if there is any error messages
    # go back to the index page with the error message.
    user = bn.get_user(session['logged_in'])
    tickets = bn.get_all_tickets()
    if error_message:
        return render_template('index.html', message=error_message, user=user, tickets=tickets)
    else:
        return redirect('/')


def update_post():
    user_email = session['logged_in']
    ticket_name = request.form.get('update-name')
    ticket_quantity = int(request.form.get('update-quantity'))
    ticket_price = int(request.form.get('update-price'))
    ticket_date = int(request.form.get('update-date'))
    error_message = None

    if (ticket_name_check(ticket_name) is None):  # no match in regex
        error_message = 'Ticket name is incorrect'

    elif quantity_check(ticket_quantity):
        error_message = "Invalid quantity in ticket update form"

    elif price_check(ticket_price):
        error_message = "Invalid price in ticket update form"

    elif date_check(ticket_date):
        error_message = "Invalid date in ticket update form"

    else:
        error_message = bn.update_ticket(user_email, ticket_name, ticket_quantity, ticket_price, ticket_date)

    return error_message


def buy_post():
    user_email = session['logged_in']
    ticket_name = request.form.get('buy-name')
    ticket_quantity = int(request.form.get('buy-quantity'))
    error_message = None
    tik = bn.get_ticket(ticket_name)
    
    if (ticket_name_check(ticket_name) is None):  # no match in regex
        error_message = 'Ticket name is incorrect'

    elif quantity_check(ticket_quantity):
        error_message = "Invalid quantity in ticket buy form"

    elif not tik:
        return "Ticket does not exist"

    elif tik.quantity < ticket_quantity:
        return "Not enough tickets for sale"

    elif bn.get_balance(user_email) < (tik.price * ticket_quantity * 1.40):
        return "Insufficient balance"

    else:
        error_message = bn.buy_ticket(user_email, ticket_name, ticket_quantity)

    return error_message


def sell_post():
    email  = session['logged_in']
    name = request.form.get('sell-name')
    quantity = int(request.form.get('sell-quantity'))
    price = int(request.form.get('sell-price'))
    expiry = (request.form.get('sell-date'))
    tickets = bn.get_all_tickets()

    if ticket_name_check(name) is None:  # no match in regex
        error_message = 'ticket name format is incorrect'

    elif quantity_check(quantity):
        error_message = "quantity format is incorrect"

    elif price_check(price):
        error_message = "price format is incorrect"

    elif date_check(expiry):
        error_message = "date format is incorrect"

    else:
        error_message = bn.set_ticket(email, name, quantity, price, expiry)

    return error_message

def ticket_name_check(name):
    if name != None:
        # regex to check ticket name is alphanumeric
        regex = '^[a-zA-Z0-9]+[a-zA-Z0-9 ]?[a-zA-Z0-9]+$'
        # check ticket name is under maximum length, include optional check for min char length
        if 6 <= len(name) < 60:
            return re.match(regex, name)


def quantity_check(quantity):
    if quantity is not None:
        return quantity <= 0 or quantity > 100
    return True


def price_check(price):
    if price is not None:
        return price < 10 or price > 100
    return True


def date_check(expiry):
    if expiry is not None:
        if len(str(expiry)) != 8:  # check if in proper format length
            return True
        elif int(str(expiry)[4:6]) <= 0 or int(str(expiry)[4:6]) > 12: # check month format
            return True
        elif int(str(expiry)[6:8]) <= 0 or int(str(expiry)[6:8]) > 31: # check day format
            return True
        else:
            return int(expiry) < int(date.today().strftime("%Y%m%d"))  # check if expiry is before today
    return True