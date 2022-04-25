from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """
    user = get_user(email)
    if user:
        return "This email has been ALREADY used"

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)

    db.session.add(new_user)
    db.session.commit()
    return None

def set_ticket(owner, name, quantity, price, date):
    """
    Register a ticket to the database
    :param owner: the email of the ticket seller
    :param name: the name of the ticket
    :param quantity: the quantity of tickets being sold
    :param price: the price of each ticket being sold
    :param date: the date the tickets expire
    :return: an error message if there is any, or None if register succeeds
    """
    new_ticket = Ticket(owner=owner, name=name, quantity=quantity, price=price, date=date)

    db.session.add(new_ticket)
    db.session.commit()
    return None


def get_all_tickets():
    """
    Gets all the tickets in the database that havent expired
    :return: a list of Tickets that havent expired
    """
    tik = Ticket.query.filter(Ticket.date > int(date.today().strftime('%Y%m%d'))).all()
    return tik

def update_ticket(owner, name, quantity, price, date):
    """
    Attempt to update a ticket in the database
    :return: an error message if there is any, or None if update succeeds
    """
    tik = Ticket.query.filter_by(owner=owner, name=name).first()
    if not tik:
        return "Ticket does not exist"
    tik.quantity = quantity
    tik.price = price
    tik.date = date
    db.session.commit()
    return None

def buy_ticket(email, name, quantity):
    """
    Attmempt to buy a ticket in the database
    :param owner: the email of the ticket buyer
    :param name: the name of the ticket being bought
    :param quantity: the quantity of tickets being bought
    :return: an error message if there is any, or None if register succeeds
    """
    user = User.query.filter_by(email=email).first()
    tik = Ticket.query.filter_by(name=name).first()
    user.balance = user.balance - (tik.price * quantity * 1.40)
    if tik.quantity == quantity:
        db.session.delete(tik)
    else:
        tik.quantity = tik.quantity - quantity
    db.session.commit()
    return None

def delete_database():
    """
    Deletes both the Ticket and User databases
    """
    User.query.delete()
    Ticket.query.delete()
    db.session.commit()

def get_ticket(name):
    """
    Gets the first ticket in the database
    :param name: the name of the ticket
    :return: The ticket or none if no ticket exist 
    """
    return Ticket.query.filter_by(name=name).first()

def get_balance(owner):
    """
    Gets the users current balance
    :param owner: the email of the owner
    :return: balance of the current user or none if owner doesn't exists
    """
    return User.query.filter_by(email=owner).first().balance
