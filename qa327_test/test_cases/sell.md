# Test Cases for `/sell`

| Test Case ID | Target Spec | Purpose  |
|--------------|-------------|----------|
| R4.1  | [POST] `/sell`  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character  |
| R4.1a  | [POST] `/sell`  | Ticket name with special characters produces an error message.  |
| R4.1b  | [POST] `/sell`  | Ticket name with leading space produces an error message.  |
| R4.1c  | [POST] `/sell`  | Ticket name with trailing space produces an error message.  |
| R4.2  | [POST] `/sell`  | The name of the ticket is no longer than 60 characters  |
| R4.3  | [POST] `/sell`  | The quantity of the tickets has to be more than 0, and less than or equal to 100  |
| R4.3a  | [POST] `/sell`  | Ticket quantity of 0 or less produces an error message.  |
| R4.3b  | [POST] `/sell`  | Ticket quantity of over 100 produces an error message.  |
| R4.4  | [POST] `/sell`  | Price has to be of range [10, 100]  |
| R4.4a  | [POST] `/sell`  | Price of less than 10 produces an error message.  |
| R4.4b  | [POST] `/sell`  | Price of greater than 100 produces an error message.  |
| R4.5  | [POST] `/sell`  | Date must be given in the format YYYYMMDD (e.g. 20200901)  |
| R4.5a  | [POST] `/sell`  | Mis-formatted date produces error message.  |
| R4.5b  | [POST] `/sell`  | Date in the past produces error message.  |
| R4.6  | [POST] `/sell`  | For any errors, redirect back to / and show an error message  |
| R4.7  | [POST] `/sell`  | The added new ticket information will be posted on the user profile page  |

# Test Plans for `/sell`

To setup for each test case, the following will be completed prior to the test case actions(omitted from each test case for brevity):

### Test data 
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Password!')
    );
```

### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- enter valid test_user data in `#email` and `#password` elements
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200
- verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R4.1a
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

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.1b
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
- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.1c
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

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.2
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

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.3a
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

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.3b
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

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.4a
**Price has to be of range [10, 100].**  
Price of less than 10 produces an error message.

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

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.b
**Price has to be of range [10, 100].**  
Price of greater than 100 produces an error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='1',
        price='150',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.5a
**Date must be given in the format YYYYMMDD (e.g. 20200901).**  
Mis-formatted date produces error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='1',
        price='20',
        date='01012020',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`

## Test Case R4.5b
**Date must be given in the format YYYYMMDD (e.g. 20200901).**  
Date in the past produces error message.

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='1',
        price='20',
        date='20100901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 400 response
- verify profile page displays error message by checking content of `#message`


## Test Case R4.6
**For any errors, redirect back to / and show an error message.**  

This is checked in cases R4.1-R4.5

## Test Case R4.7
**The added new ticket information will be posted on the user profile page.**

### Test Data:
```
    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket',
        quantity='1',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_ticket to return a test_ticket instance

### Actions

- click on `#ticket-name` element and enter `test_ticket.name`
- click on `#quantity` element and enter `test_ticket.quantity`
- click on `#price` element and enter `test_ticket.price`
- click on `#date` element and enter `test_ticket.date`
- click on `#ticket-submit` to submit the form 
- verify that [POST] `/sell` was called with 200
- verify that user is navigated to `/` profile page
- verify that profile page displays test_ticket information
