# Test Cases for `/buy`

| Test Case ID | Target Spec | Purpose  |
|--------------|-------------|----------|
| R6.1 | [POST] `/buy`  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.  |
| R6.1a | [POST] `/buy`  | Ticket name with special characters produces an error message.  |
| R6.1b | [POST] `/buy`  | Ticket name with leading space produces an error message.  |
| R6.1c | [POST] `/buy`  | Ticket name with trailing space produces an error message.  |
| R6.2 | [POST] `/buy`  | The name of the ticket is no longer than 60 characters  |
| R6.3 | [POST] `/buy`  | The quantity of the tickets has to be more than 0, and less than or equal to 100  |
| R6.3a | [POST] `/buy`  | Ticket quantity of 0 or less produces an error message.  |
| R6.3b | [POST] `/buy`  | Ticket quantity of over 100 produces an error message.  |
| R6.4a | [POST] `/buy` | The ticket name exists in the database and the quantity is more than the quantity requested to buy(positive). |
| R6.4b | [POST] `/buy` | The ticket name exists in the database and the quantity is less than the quantity requested to buy(negative). |
| R6.4c | [POST] `/buy` | The ticket does not exists in the database and the quantity is more than the quantity requested to buy(negative). |
| R6.5a | [POST] `/buy` | The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)(positive). |
| R6.5b | [POST] `/buy` | The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)(negative). |
| R6.6 | [POST] `/buy` | For any errors, redirect back to / and show an error message |


# Test Plans for `/buy`

To setup for each test case, the following will be completed prior to the test case actions(omitted from each test case for brevity):

### Test data 
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Password!')
        balance ='30'
    );
```

### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- enter valid `test_user.email` data in `#email` element
- enter valid `test_user.password` data in `#email` element
- click on `#btn_submit` element to login
- verify that [POST] `/login` was called with 200
- navigate to `/`

## Test Case R6.1a
**The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.**  
Ticket name with special characters produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket!@#',
        quantity='1',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.1b
**The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.**  
Ticket name with leading space produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name=' test ticket',
        quantity='1',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.1c
**The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.**  
Ticket name with trailing space produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket ',
        quantity='1',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.2
**The name of the ticket is no longer than 60 characters.**  
Ticket name longer than 60 characters produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='0123456789012345678901234567890123456789012345678901234567890',
        quantity='1',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.3a
**The quantity of the tickets has to be more than 0, and less than or equal to 100.**  
Ticket quantity of 0 or less produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='0',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form 
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.3b
**The quantity of the tickets has to be more than 0, and less than or equal to 100.**  
Ticket quantity of over 100 produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='150',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form 
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.4a
**The ticket name exists in the database and the quantity is more than the quantity requested to buy (positive).**  
Ticket name and quantity requested to buy are in the database

## Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='10',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays message `sucessful` by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.4b
**The ticket name exists in the database and the quantity is less than the quantity requested to buy (negative).**  
Ticket name not in the database produces an error message.

## Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='bad test ticket',
        quantity='10',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.4c
**The ticket name exists in the database and the quantity is less than the quantity requested to buy (negative).**  
Ticket quantity requested is more then available in database

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='1',
        price='5',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#bu_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message by checking content of `#message`
- verify that `test_ticket` shows in `\` all available tickets
- navigate to `/logout` (clean up)

## Test Case R6.5a
**The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) (positive).**  
User has enough balance to buy tickets

## Test Data:

```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='2',
        price='5',
        date='20200901',
    );
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 200 response
- verify profile page displays message `sucessful` by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.5b
**The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) (negative).**  
User does not have enough balance to buy tickets

## Test Data:

```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='2',
        price='40',
        date='20200901',
    );
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- click on `#buy_name` element and enter `test_ticket.name`
- click on `#buy_quantity` element and enter `test_ticket.quantity`
- click on `#buy_submit` to submit the form
- verify that [POST] `/buy` was called with 400 response
- verify profile page displays error message `insufficient balance` by checking content of `#message`
- navigate to `/logout` (clean up)

## Test Case R6.6
**For any errors, redirect back to / and show an error message.**  

This is checked in cases R6.1-R6.5
