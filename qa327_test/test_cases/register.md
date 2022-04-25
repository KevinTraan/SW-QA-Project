# Test Cases for `/register`

| Test Case ID | Target Spec        | Purpose                                                                                                                                |
|--------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| R2.1         | [GET] `/register`  | If the user has logged in, redirect back to the user profile page                                                                      |
| R2.2         | [GET] `/register`  | otherwise, show the user registration page                                                                                             |
| R2.3         | [GET] `/register`  | the registration page shows a registration form requesting: email, user name, password, password2                                      |
| R2.4         | [POST] `/register` | The registration form can be submitted as a POST request to the current URL (/register)                                                |
| R2.5         | [POST] `/register` | Email, password, password2 all have to satisfy the same required as defined in R1                                                      |
| R2.5a        | [POST] `/register` | Email cannot be empty                                                                                                                  |
| R2.5b        | [POST] `/register` | Password cannot be empty                                                                                                               |
| R2.5c        | [POST] `/register` | Password2 cannot be empty                                                                                                              |
| R2.5d        | [POST] `/register` | Email has to follow addr-spec defined in RFC 5322                                                                                      |
| R2.5e        | [POST] `/register` | Password has to meet the required complexity: minimum length 6                                                                         |
| R2.5f        | [POST] `/register` | Password has to meet the required complexity: at least one upper case                                                                  |
| R2.5g        | [POST] `/register` | Password has to meet the required complexity: least one lower case                                                                     |
| R2.5h        | [POST] `/register` | Password has to meet the required complexity: at least one special character                                                           |
| R2.6         | [POST] `/register` | Password and password2 have to be exactly the same                                                                                     |
| R2.7         | [POST] `/register` | Username has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.                  |
| R2.7a        | [POST] `/register` | Username has to be non-empty.                                                                                                          |
| R2.7b        | [POST] `/register` | Username has to be alphanumeric-only.                                                                                                  |
| R2.7c        | [POST] `/register` | Username is not allowed if the first character is space.                                                                               |
| R2.7d        | [POST] `/register` | Username is not allowed if the last character is space.                                                                                |
| R2.8         | [POST] `/register` | User name has to be longer than 2 characters and less than 20 characters.                                                              |
| R2.8a        | [POST] `/register` | User name has to be longer than 2 characters.                                                                                          |
| R2.8b        | [POST] `/register` | User name has to be less than 20 characters.                                                                                           |
| R2.9         | [POST] `/register` | For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)      |
| R2.10        | [POST] `/register` | If the email already exists, show message 'this email has been ALREADY used'                                                           |
| R2.11        | [POST] `/register` | If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page |

# Test Plans for `/register`

## Test Case R2.1
**If the user has logged in, redirect back to the user profile page**

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

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Enter `test_user.email` in `#email` element
- Enter `test_user.password` in `#password` element
- Click on `#btn-submit` element
- Navigate to /register
- Verify that profile page is visible by checking for `#welcome-header` element in DOM

## Test Case R2.2
**otherwise, show the user registration page**

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Verify that register page is visible by checking for expected elements (eg. `form-group`) in DOM

## Test Case R2.3
**the registration page shows a registration form requesting: email, user name, password, password2**

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Verify that `#email`, `#username`, `#password`, and `#password2` elements exist in the DOM

## Test Case R2.4
**The registration form can be submitted as a POST request to the current URL (/register)**

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM

## Test Case R2.5a
**Email, password, password2 all have to satisfy the same required as defined in R1**
Email cannot be empty

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.5b
**Email, password, password2 all have to satisfy the same required as defined in R1**
Password cannot be empty

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.5c
**Email, password, password2 all have to satisfy the same required as defined in R1**
Password2 cannot be empty

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.5d
**Email, password, password2 all have to satisfy the same required as defined in R1**
Email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation)

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter “not.@.valid@email_address.com” in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element

## Test Case R2.5e
**Email, password, password2 all have to satisfy the same required as defined in R1**
Password has to meet the required complexity: minimum length 6

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter “$Mall” in `#password` element
- Enter “$Mall” in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.5f
**Email, password, password2 all have to satisfy the same required as defined in R1**
Password has to meet the required complexity: at least one upper case

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter “lowerc@se” in `#password` element
- Enter “lowerc@se” in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.5g
**Email, password, password2 all have to satisfy the same required as defined in R1**
Password has to meet the required complexity: least one lower case

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter “UPPERC@SE” in `#password` element
- Enter “UPPERC@SE” in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.5h
**Email, password, password2 all have to satisfy the same required as defined in R1**
Password has to meet the required complexity: at least one special character

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter “noSpecial” in `#password` element
- Enter “noSpecial” in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.6
**Password and password2 have to be exactly the same**

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a different valid password (e.g. “AlsoValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.7a
**User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.**
Username has to be non-empty.

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.7b
**User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.**
Username has to be alphanumeric-only.

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter “#alphanumer” in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.7c
**User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.**
Username is not allowed if the first character is space.

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter “ firstchar” `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.7d
**User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.**
Username is not allowed if the last character is space.

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter “lastchara ” `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.8a
**User name has to be longer than 2 characters and less than 20 characters.**
Username has to be longer than 2 characters.

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter “2C” `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.8b
**User name has to be longer than 2 characters and less than 20 characters.**
Username has to be less than 20 characters.

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter “twentycharacterslong” `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays error message by checking content of `#message`

## Test Case R2.9
**For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)**

This is checked in cases R2.5 – R2.8

## Test Case R2.10
**If the email already exists, show message 'this email has been ALREADY used'**

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

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter `test_user.email` in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Verify current page displays email in use message by checking content of `#message`

## Test Case R2.11
**If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page**

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Navigate to /register
- Enter a valid username (e.g. “Valid Username”) in `#username` element
- Enter a valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password` element
- Enter a valid password (e.g. “ValidP@ssword”) in `#password2` element
- Click on `#btn-submit` element
- Enter the same valid email address (e.g. “valid.email@address.com”) in `#email` element
- Enter the same valid password (e.g. “ValidP@ssword”) in `#password` element
- Click on `#btn-submit` element
- Verify current page displays balance at 5000 by checking content of `#balance_message`