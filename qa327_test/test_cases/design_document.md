# Design Document

## Architecture

| Classes          | Description                                        |
|------------------|----------------------------------------------------|
| User(db.Model)   | Contains all stored information for a given user   |
| Ticket(db.Model) | Contains all stored information for a given ticket |

| Layer    | Methods                                           | Description                                                           |
|----------|---------------------------------------------------|-----------------------------------------------------------------------|
| Frontend | register_get()                                    | Renders register page if not logged in                                |
| Frontend | register_post()                                   | Attempts to register with supplied new user information               |
| Frontend | login_get()                                       | Renders login page with a login message                               |
| Frontend | login_post()                                      | Attempts to login with an email and password                          |
| Frontend | authenticate(inner_function)                      | Wrapper, authenticates user before allowing access to other functions |
| Frontend | profile(user)                                     | Renders user’s profile page and tickets menu                          |
| Frontend | email_check(email)                                | Verifies format of email passed in                                    |
| Frontend | pwd_check(password)                               | Verifies format of password passed in                                 |
| Frontend | username_check(name)                              | Verifies format of username passed in                                 |
| Frontend | update_post()                                     | Attempts to update an existent ticket                                 |
| Frontend | buy_post()                                        | Attempts to buy an existent ticket                                    |
| Frontend | sell_post()                                       | Attempts to sell an existent ticket                                   |
| Frontend | ticket_name_check(name)                           | Verifies format of ticket name passed in                              |
| Frontend | quantity_check()(quantity)                        | Verifies quantity of ticket is in range (0,100]                       |
| Frontend | price_check(price)                                | Verifies price of ticket is in range [10,100]                         |
| Frontend | date_check(expiry)                                | Verifies expiry date of ticket is in proper format and not expired    |
| Frontend | form_button()                                     | Checks what button(sell/buy/update)is clicked and calls that function |
| Backend  | get_user(email)                                   | Attempt to return user based on supplied email                        |
| Backend  | login_user(email, password)                       | Attempt to authenticate user’s login                                  |
| Backend  | register_user(email, name, password, password2)   | Attempt to register new user to the database                          |
| Backend  | get_all_tickets()                                 | Return all non-expired tickets from database                          |
| Backend  | set_ticket(owner, name, quantity, price, date)    | Attempt to register a new ticket to the database                      |
| Backend  | update_ticket(owner, name, quantity, price, date) | Attempt to update a ticket in the database                            |
| Backend  | buy_ticket(email, name, quantity)                 | Attempt to buy a ticket in the database                               |
| Backend  | delete_database()                                 | Deletes all data inside the User and Ticket databases                 |
| Backend  | get_ticket(name)                                  | Attempt to get the first ticket in the database                       |
| Backend  | get_balance(owner)                                | Attempt to get the balance of the owner                               |


## Test Plan

**How test cases of different levels (frontend, backend units, integration) are organized.**

- The frontend and backend unit tests will be located under the `/qa327_test/frontend` and `/qa327_test/backend` folders.
- The integration tests are located under the `/qa327_test/integration` folder.
- Each unit test will have it's own python test file to work best with Pytest
- Example: in `/qa327_test/frontend` would be `test_register` which has all the tests for the `/register` methods

**The order to the test cases (which level first which level second).**

- First Level: Individual method testing done locally and manually
- Second Level: Unit testing (frontend and backend) done locally, automated via Pytest
- Third Level: Integration testing done locally, automated via Pytest
- Fourth Level: Full system testing done via Github Actions

**Techniques and tools used for testing.**

- The frontend and backend components will be integration tested using Selenium.
- Tests will be run locally as they are written, and must be passing on GitHub Actions before merging to master.
- The methods listed above will be tested at the unit test level using multiple inputs and verifying the output.

**Environments (all the local environment and the cloud environment) for the testing.**

- The environment used for testing will be...
- Windows 10 ver.2004 (local)
- Windows 10 ver.1903 (local)
- MacOS 10.15.4 (local)
- Ubuntu 18.04 (cloud)
- exclusively using the Chrome browser

**Responsibility (who is responsible for which test case, and in case of failure, who should you contact)**

- The developer that wrote the test cases in A1 will be responsible for writing and maintaining test cases.

| Test Case     | Contact |
|---------------|---------|
| R1 - /login   | Vivian  |
| R2 - /register| Adrian  |
| R3 - /        | Kevin   |
| R4 - /sell    | Vivian  |
| R5 - /update  | Adrian  |
| R6 - /buy     | Kevin   |
| R7 - /logout  | Adrian  |
| R8 - /*       | Adrian  |

**Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unnecessary cost)**

- GitHub can send a usage report with a summary of GitHub Actions minutes used to the repository owner. An example report for the last 30 days is below.
- The repository owner can check how many action minutes are left and notify the rest of the team if there's a chance we'll hit the limit
- To minimize the amount of unnecessary action minutes used, the entire test suite will first be run locally to ensure everything passes before being pushed to Github.
- Can also skip running the CI if no code was changed

| Date       | Product | Repository Slug | Quantity | Unit Type | Price Per Unit | Actions Workflow             |
| ---------- | ------- | --------------- | -------- | --------- | -------------- | ---------------------------- |
| 2020-10-09 | actions | 15vrs/cmpe-327  | 1        | UBUNTU    | $0.01          | .github/workflows/maven.yml  |
| 2020-10-09 | actions | 15vrs/cmpe-327  | 14       | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-10-12 | actions | 15vrs/cmpe-327  | 6        | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-10-13 | actions | 15vrs/cmpe-327  | 6        | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-10-14 | actions | 15vrs/cmpe-327  | 12       | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-10-15 | actions | 15vrs/cmpe-327  | 4        | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-10-16 | actions | 15vrs/cmpe-327  | 2        | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-10-17 | actions | 15vrs/cmpe-327  | 28       | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-11-03 | actions | 15vrs/cmpe-327  | 10       | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-11-04 | actions | 15vrs/cmpe-327  | 26       | UBUNTU    | $0.01          | .github/workflows/python.yml |
| 2020-11-06 | actions | 15vrs/cmpe-327  | 8        | UBUNTU    | $0.01          | .github/workflows/python.yml |
