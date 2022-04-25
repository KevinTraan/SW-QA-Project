# Test Cases for `/logout`

| Test Case ID | Target Spec          | Purpose                                                                                                                                      |
|--------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| R7.1         | [GET,POST] `/logout` | Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages. |
| R7.1a        | [GET,POST] `/logout` | Basic logout invalidates the current session check                                                                                           |
| R7.1b        | [GET,POST] `/logout` | Advanced logout invalidates the current session check                                                                                        |
| R7.1c        | [GET,POST] `/logout` | After logout user can't access restricted pages                                                                                              |

# Test Plans for `/logout`

## Test Case R7.1a
**Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.**
Basic logout invalidates the current session check

### Actions:

- Navigate to /logout
- Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM

## Test Case R7.1b
**Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.**
Advanced logout invalidates the current session check

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

### Actions:

- Navigate to /logout
- Navigate to /login
- Enter `test_user.email` in `#email` element
- Enter `test_user.password` in `#password` element
- Click on `#btn-submit` element
- Navigate to /logout
- Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM 

## Test Case R7.1c
**Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.**
After logout user can’t access restricted pages

### Actions:

- Navigate to /logout
- Navigate to /
- Verify that login page is visible by checking expected elements (eg. `form-group`) in DOM 