# Test Cases for `buy_ticket`

| Path | Statements    | Email                   | Name        | Quantity |
|------|---------------|-------------------------|-------------|----------|
| P1   | 1,2,3,4,5,7,8 | test_user@test.com      | Test Ticket | 32       |
| P2   | 1,2,3,4,6,7,8 | test_user@test.com      | Test Ticket | 5        |

# Test Plans for `buy_ticket`

For all test cases below, the following test data must be in the repository:

### Test data 
```
	User(
        email='test_user@test.com',
        name='test_user',
        password=generate_password_hash('Password!'),
        balance=5000
	);

	Ticket(
		owner = 'test_frontend@test.com',
		name = 'Test Ticket',
		quantity = '32',
		price = '20',
		date = '20210901'
	);
```

## Test case 1
Path: P1
Input:
	- email = `test_user@test.com`
	- name = `Test Ticket`
	- quantity = `32`
Output: None

## Test case 2
Path: P2
Input:
	- email = `test_user@test.com`
	- name = `Test Ticket`
	- quantity = `5`
Output: None