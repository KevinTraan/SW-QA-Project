# Test Cases for `/`

| Test Case ID | Target Spec | Purpose  |
|--------------|-------------|----------|
| R3.1 | [GET] `/`  | If the user hasn't logged in, redirect the login page  |
| R3.2 | [GET] `/`  | This page shows a header 'Hi {}'.format(user.name) |
| R3.3 | [GET] `/`  | This page shows user balance. |
| R3.4 | [GET] `/`  | This page shows a logout link, pointing to /logout |
| R3.5 | [GET] `/`  | This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. |
| R3.6 | [GET] `/`  | This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date. |
| R3.7 | [GET] `/`  | This page contains a form that a user can buy new tickets. Fields: name, quantity |
| R3.8 | [GET] `/`  |This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date |
| R3.9 | [GET] `/`  | The ticket-selling form can be posted to /sell |
| R3.10 | [GET] `/`  | The ticket-buying form can be posted to /buy |
| R3.11 | [GET] `/` | The ticket-update form can be posted to /update |

# Test Plans for `/`

## Test Case R3.1
**If the user hasn't logged in, redirect the login page.**  

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking expected elements (eg. `form-group`) in DOM

## Test Case R3.2
**This page shows a header 'Hi {}'.format(user.name)**  

## Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking expected elements (eg. `form-group`) in DOM
- verify that user is navigated to `/`
- verify that `/` shows header `'Hi test_frontend'`
- navigate to `/logout` (clean up)

## Test Case R3.3
**This page shows user balance.**  

## Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows the users balance `'Balance: 30'`
- navigate to `/logout` (clean up)

## Test Case R3.4
**This page shows a logout link, pointing to /logout.**  

## Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a logout link `'logout'` pointing to `/logout`
- navigate to `/logout` (clean up)

## Test Case R3.5
**This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a list of all available tickets in the database that are not expired
- verify that the information displayed is accurate by checking the quantity, owner's email, and price are all accurate
- navigate to `/logout` (clean up)

## Test Case R3.6
**This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a form to submit new tickets for sell with fields `#sell-name`, `#sell-quantity`, `#sell-price`, `#sell-date`
- navigate to `/logout` (clean up)

## Test Case R3.7
**This page contains a form that a user can buy new tickets. Fields: name, quantity.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a form to buy new tickets with fields `#sell-name`, `#sell-quantity`
- navigate to `/logout` (clean up)

## Test Case R3.8
**This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- verify that `/` shows a form to update existing tickets with fields `#name-name`, `#update-quantity`, `#update-price`, `#update-date`

## Test Case R3.9
**The ticket-selling form can be posted to /sell.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- click on `#sell-name` and enter `test_ticket.name`
- click on `#sell-quantity` and enter `test_ticket.quantity`
- click on `#sell-price` and enter `test_ticket.price`
- click on `#sell-date` and enter `test_ticket.date`
- click on `#sell-submit` to submit the form
- verify that [POST] `/sell` was called with 200
- navigate to `/logout` (clean up)

## Test Case R3.10
**The ticket-buying form can be posted to /buy.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- click on `#buy-ticket_name` and enter `test_ticket.name`
- click on `#buy-quantity` and enter `test_ticket.quantity`
- click on `#buy-submit` to submit the form
- verify that [POST] `/buy` was called with 200
- navigate to `/logout` (clean up)

## Test Case R3.11
**The ticket-update form can be posted to /update.**  

## Test Data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password!')
    balance = '30'
)

test_ticket = Ticket(
    owner='test_seller@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```
### Mocking:  

- mock backend.get_user to return a test_user instance
- mock backend.get_ticket to return a test_ticket instance

### Actions  

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- open `/`
- verify that user is navigated to `/`
- click on `#update_ticket_name` and enter `test_ticket.name`
- click on `#update_quantity` and enter `test_ticket.quantity`
- click on `#update_price` and enter `test_ticket.price`
- click on `#update_date` and enter `test_ticket.date`
- click on `#update_submit` to submit the form
- verify that [POST] `/update` was called with 200
- navigate to `/logout` (clean up)