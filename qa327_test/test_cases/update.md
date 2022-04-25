# Test Cases for `/update`

| Test Case ID | Target Spec      | Purpose                                                                                                                  |
|--------------|------------------|--------------------------------------------------------------------------------------------------------------------------|
| R5.1         | [POST] `/update` | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
| R5.1a        | [POST] `/update` | The name of the ticket must be alphanumeric-only.                                                                        |
| R5.1b        | [POST] `/update` | The name of the ticket is not allowed if the first character is a space.                                                 |
| R5.1c        | [POST] `/update` | The name of the ticket is not allowed if the last character is a space.                                                  |
| R5.2         | [POST] `/update` | The name of the ticket is no longer than 60 characters                                                                   |
| R5.3         | [POST] `/update` | The quantity of the tickets has to be more than 0, and less than or equal to 100.                                        |
| R5.3a        | [POST] `/update` | The quantity of the tickets has to be more than 0.                                                                       |
| R5.3b        | [POST] `/update` | The quantity of the tickets has to be less than or equal to 100.                                                         |
| R5.4         | [POST] `/update` | Price has to be of range [10, 100]                                                                                       |
| R5.4a        | [POST] `/update` | Price has to be greater than or equal to 10.                                                                             |
| R5.4b        | [POST] `/update` | Price has to be less than or equal to 100.                                                                               |
| R5.5         | [POST] `/update` | Date must be given in the format YYYYMMDD (e.g. 20200901)                                                                |
| R5.5a        | [POST] `/update` | Year must be formatted properly.                                                                                         |
| R5.5b        | [POST] `/update` | Month must be formatted properly.                                                                                        |
| R5.5c        | [POST] `/update` | Day must be formatted properly.                                                                                          |
| R5.5d        | [POST] `/update` | Date must not have passed.                                                                                               |
| R5.6         | [POST] `/update` | The ticket of the given name must exist                                                                                  |
| R5.7         | [POST] `/update` | For any errors, redirect back to / and show an error message                                                             |
| R5.7a        | [POST] `/update` | An update with an error displays an error message                                                                        |
| R5.7b        | [POST] `/update` | An update without errors passes successfully                                                                             |

# Test Plans for `/update`

For all test cases below, the following steps must be completed (omitted for brevity):

### Test data 
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Password!')
    );

    test_ticket = Ticket(
        owner='test_frontend@test.com',
        name='test ticket!@#',
        quantity='1',
        price='20',
        date='20200901',
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Enter `test_user.email` in `#email` element
- Enter `test_user.password` in `#password` element
- Click on `#btn-submit` element
- Navigate to /

## Test Case R5.1a
**The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.**
The name of the ticket must be alphanumeric-only.

### Actions:

- Enter “#invalidticket” into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.1b
**The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.**
The name of the ticket is not allowed if the first character is a space.

### Actions:

- Enter “ firstchar” into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.1c
**The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.**
The name of the ticket is not allowed if the last character is a space.

### Actions:

- Enter “lastchar ” into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.2
**The name of the ticket is no longer than 60 characters**

### Actions:

- Enter “unfortunatelythistickethasalittleoversixtycharactersinitsname” into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)


## Test Case R5.3a
**The quantity of the tickets has to be more than 0, and less than or equal to 100.**
The quantity of the tickets has to be more than 0.

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter “0” into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.3b
**The quantity of the tickets has to be more than 0, and less than or equal to 100.**
The quantity of the tickets has to be less than or equal to 100.

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter “101” into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.4a
**Price has to be of range [10, 100]**
 Price has to be greater than or equal to 10.
 
### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter “9” into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.4b
**Price has to be of range [10, 100]**
 Price has to be less than or equal to 100.
 
### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter “101” into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.5a
**Date must be given in the format YYYYMMDD (e.g. 20200901)**
Year must be formatted properly.

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter “170901” into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.5b
**Date must be given in the format YYYYMMDD (e.g. 20200901)**
Month must be formatted properly.

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter “20202001” into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.5c
**Date must be given in the format YYYYMMDD (e.g. 20200901)**
Day must be formatted properly.

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter “20201232” into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.5d
**Date must be given in the format YYYYMMDD (e.g. 20200901)**
Date must not have passed.

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter “19870101” into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.6
**The ticket of the given name must exist**

### Actions:

- Enter “anonexistentticket” into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `test_ticket.price` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays error message by checking content of `#message`
- Navigate to /logout (clean up)

## Test Case R5.7a
**For any errors, redirect back to / and show an error message**
An update with an error displays an error message

This is checked in cases R5.1 - R5.6

## Test Case R5.7b
**For any errors, redirect back to / and show an error message**
An update without errors passes successfully

### Actions:

- Enter `test_ticket.name` into `#update_name` element 
- Enter `test_ticket.quantity` into `#update_quantity` element 
- Enter `22` into `#update_price` element 
- Enter `test_ticket.date` into `#update_date` element 
- Click on `#update-submit` element
- Verify profile page displays updated test_ticket information
- Navigate to /logout (clean up)