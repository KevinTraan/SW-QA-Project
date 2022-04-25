# Test Cases for `/*`

| Test Case ID | Target Spec | Purpose                                                                                 |
|--------------|-------------|-----------------------------------------------------------------------------------------|
| R8.1         | [any] `/*`  | For any other requests except the ones above, the system should return a 404 error      |
| R8.1a        | [any] `/*`  | When not logged in return a 404 error for any other requests except the authorized ones |
| R8.1b        | [any] `/*`  | When logged in return a 404 error for any other requests except the authorized ones     |
| R8.1c        | [any] `/*`  | When not logged in ensure a 404 error is not sent for the authorized requests           |
| R8.1d        | [any] `/*`  | When logged in ensure a 404 error is not sent for the authorized requests               |

# Test Plans for `/*`

## Test Case R8.1a
**For any other requests except the ones above, the system should return a 404 error**
When not logged in return a 404 error for any other requests except the authorized ones

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /badrequest
- Verify current page displays 404 error message by checking content of `#message`

## Test Case R8.1b
**For any other requests except the ones above, the system should return a 404 error**
When logged in return a 404 error for any other requests except the authorized ones

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

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Enter `test_user.email` in `#email` element
- Enter `test_user.password` in `#password` element
- Click on `#btn-submit` element
- Navigate to /badrequest
- Verify current page displays 404 error message by checking content of `#message`

## Test Case R8.1c
**For any other requests except the ones above, the system should return a 404 error**
When not logged in ensure a 404 error is not sent for the authorized requests

### Actions:

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Verify current page does not display the 404 error message by checking content of `#message`

## Test Case R8.1d
**For any other requests except the ones above, the system should return a 404 error**
When logged in ensure a 404 error is not sent for the authorized requests

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

- Navigate to /logout (Invalidate any logged-in sessions)
- Navigate to /login
- Enter `test_user.email` in `#email` element
- Enter `test_user.password` in `#password` element
- Click on `#btn-submit` element
- Navigate to /
- Verify current page does not display the 404 error message by checking content of `#message`