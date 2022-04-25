# Test Cases for Backend

| Method     | Inputs          | Output |
|------------|-----------------|--------|
| get_user   | email           | user   |
| login_user | email, password | user   |
|            |                 |        |

# Test cases for `get_user`

## Test case 1.1
Partition: valid email of registered user returns valid user
Input:
    - email = `test_frontend@test.com`
Output: 
 ```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Password!'),
        balance=5000
    );
```

## Test case 1.2
Partition: valid email of unregistered user returns None
Input:
    - email = `test_frontend@test.com`
Output: None

# Test cases for `login_user`

## Test case 2.1
Partition: registered user credentials can log in and returns valid user
Input:
    - email = `test_frontend@test.com`
    - password = `Password!`
Output: 
 ```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Password!'),
        balance=5000
    );
```

## Test case 2.2
Partition: unregistered user credentials cannot log in and returns None
Input:
    - email = `unregistered@test.com`
    - password = `Password!`
Output: None

## Test case 2.3
Partition: wrong password cannot log in and returns None
Input:
    - email = `test_frontend@test.com`
    - password = `WrongPassword!`
Output: None