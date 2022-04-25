# Test Cases for `/login`

| Test Case ID | Target Spec | Purpose  |
|--------------|-------------|----------|
| R1.1  | [GET] `/login`  | If the user hasn't logged in, show the login page  |
| R1.2  | [GET] `/login`  | The login page has a message that by default says 'please login'  |
| R1.3  | [GET] `/login`  | If the user has logged in, redirect to the user profile page  |
| R1.4  | [GET] `/login`  | The login page provides a login form which requests two fields: email and passwords  |
| R1.5  | [POST] `/login`  | The login form can be submitted as a POST request to the current URL  |
| R1.6 | [POST] `/login`  | Email and password both cannot be empty  |
| R1.6a  | [POST] `/login`  | Empty email and password does not login.  |
| R1.6b  | [POST] `/login`  | Empty email does not login.  |
| R1.6c  | [POST] `/login`  | Empty password does not login.  |
| R1.7  | [POST] `/login`  | Email has to follow addr-spec defined in RFC 5322  |
| R1.7a  | [POST] `/login`  | Valid email can login.  |
| R1.7b  | [POST] `/login`  | Invalid email cannot login and error message is displayed.  |
| R1.8  | [POST] `/login`  | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character  |
| R1.8a  | [POST] `/login`  | User with password shorter than 6 characters cannot log in and error message is displayed.  |
| R1.8b  | [POST] `/login`  | User with password with no uppercase characters cannot log in and error message is displayed.  |
| R1.8c  | [POST] `/login`  | User with password with no lowercase characters cannot log in and error message is displayed.  |
| R1.8d  | [POST] `/login`  | User with password with no special characters cannot log in and error message is displayed.  |
| R1.9  | [POST] `/login`  | For any formatting errors, render the login page and show the message 'email/password format is incorrect  |
| R1.10  | [POST] `/login`  | If email/password are correct, redirect to `/`  |
| R1.11  | [POST] `/login`  | Otherwise, redirect to `/login` and show message 'email/password combination incorrect'  |
| R1.11a  | [POST] `/login`  | Invalid email redirects to `/login` with error message  |
| R1.11b  | [POST] `/login`  | Invalid password redirects to `/login` with error message.  |

# Test Plans for `/login`

## Test Case R1.1
**If the user hasn't logged in, show the login page.**

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking expected elements (eg. `form-group`) in DOM

## Test Case R1.2
**The login page has a message that by default says 'please login'.**

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that 'please login' is visible by checking for the `#message' element in DOM

## Test Case R1.3
**If the user has logged in, redirect to the user profile page.**

### Test Data:
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
- verify verify that login page is visible
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R1.4
**The login page provides a login form which requests two fields: email and passwords.**

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called with 200
- verify that login page is visible by checking for expected elements (eg. `form-group`) in DOM
- verify that `#email` and `#password` elements exist in the DOM

## Test Case R1.5
**The login form can be submitted as a POST request to the current URL.**

### Test Data:
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
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200

## Test Case R1.6a
**Email and password both cannot be empty.**  
Empty email and password does not login.

### Test Data:
```
    test_user = User(
        email='',
        name='test_frontend',
        password=generate_password_hash('')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#btn-submit` element to login
- verify that login page is still visible and [POST] `/login` was not called

## Test Case R1.6b
**Email and password both cannot be empty.**  
Empty email does not login.

### Test Data:
```
    test_user = User(
        email='',
        name='test_frontend',
        password=generate_password_hash('Password!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that login page is still visible and [POST] `/login` was not called

## Test Case R1.6c
**Email and password both cannot be empty.**  
Empty password does not login.

### Test Data:
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#btn-submit` element to login
- verify that login page is still visible and [POST] `/login` was not called

## Test Case R1.7a
**Email has to follow addr-spec defined in RFC 5322.**  
Valid email can login.

### Test Data:
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
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200

## Test Case R1.7b
**Email has to follow addr-spec defined in RFC 5322.**  
Invalid email cannot login and error message 'email/password format is incorrect' is displayed.

### Test Data:
```
    test_user = User(
        email='test_frontend',
        name='test_frontend',
        password=generate_password_hash('Password!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 400
- verify login page displays error message by checking content of `#message`

## Test Case R1.8a
**Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.**  
User with password shorter than 6 characters cannot log in and error message 'email/password format is incorrect' is displayed.

### Test Data:
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Pass!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 400
- verify login page displays error message by checking content of `#message`

## Test Case R1.8b
**Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.**  
User with password with no uppercase characters cannot log in and error message 'email/password format is incorrect' is displayed.

### Test Data:
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('password!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 400
- verify login page displays error message by checking content of `#message`

## Test Case R1.8c
**Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.**  
User with password with no lowercase characters cannot log in and error message 'email/password format is incorrect' is displayed.

### Test Data:
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('PASSWORD!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 400
- verify login page displays error message by checking content of `#message`

## Test Case R1.8d
**Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.**  
User with password with no special characters cannot log in and error message 'email/password format is incorrect' is displayed.

### Test Data:
```
    test_user = User(
        email='test_frontend@test.com',
        name='test_frontend',
        password=generate_password_hash('Password')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 400
- verify login page displays error message by checking content of `#message`

## Test Case R1.9
**For any formatting errors, render the login page and show the message 'email/password format is incorrect'.**  
This is tested in cases R1.6-R1.8.

## Test Case R1.10
**If email/password are correct, redirect to `/`.**

### Test Data:
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
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 200
- verify that user is navigated to `/` profile page
- verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R1.11a
**Otherwise, redirect to `/login` and show message 'email/password combination incorrect'.**  
Invalid email redirects to `/login` with error message.

### Test Data:
```
    test_user = User(
        email='test_frontend',
        name='test_frontend',
        password=generate_password_hash('Password!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401
- verify login page displays error message by checking content of `#message`

## Test Case R1.11b
**Otherwise, redirect to `/login` and show message 'email/password combination incorrect'.**  
Invalid password redirects to `/login` with error message.

### Test Data:
```
    test_user = User(
        email='test_frontend@test.com',
        name='wrong-password',
        password=generate_password_hash('Password!')
    );
```
### Mocking:

- mock backend.get_user to return a test_user instance

### Actions

- navigate to `/logout` to invalidate any existing sessions
- navigate to `/login` and verify that [GET] `/login` was called
- click on `#email` element and enter `test_user.email`
- click on `#password` element and enter `test_user.password`
- click on `#btn-submit` element to login
- verify that [POST] `/login` was called with 401
- verify login page displays error message by checking content of `#message`