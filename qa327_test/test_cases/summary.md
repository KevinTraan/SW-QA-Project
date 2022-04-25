# Summarized Test Cases

| Test Case ID | Target Spec            | Purpose                                                                                                                                                       |
|--------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R1.1         | [GET] `/login`         | If the user hasn't logged in, show the login page                                                                                                             |
| R1.2         | [GET] `/login`         | The login page has a message that by default says 'please login'                                                                                              |
| R1.3         | [GET] `/login`         | If the user has logged in, redirect to the user profile page                                                                                                  |
| R1.4         | [GET] `/login`         | The login page provides a login form which requests two fields: email and passwords                                                                           |
| R1.5         | [POST] `/login`        | The login form can be submitted as a POST request to the current URL                                                                                          |
| R1.6         | [POST] `/login`        | Email and password both cannot be empty                                                                                                                       |
| R1.6a        | [POST] `/login`        | Empty email and password does not login.                                                                                                                      |
| R1.6b        | [POST] `/login`        | Empty email does not login.                                                                                                                                   |
| R1.6c        | [POST] `/login`        | Empty password does not login.                                                                                                                                |
| R1.7         | [POST] `/login`        | Email has to follow addr-spec defined in RFC 5322                                                                                                             |
| R1.7a        | [POST] `/login`        | Valid email can login.                                                                                                                                        |
| R1.7b        | [POST] `/login`        | Invalid email cannot login and error message is displayed.                                                                                                    |
| R1.8         | [POST] `/login`        | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character          |
| R1.8a        | [POST] `/login`        | User with password shorter than 6 characters cannot log in and error message is displayed.                                                                    |
| R1.8b        | [POST] `/login`        | User with password with no uppercase characters cannot log in and error message is displayed.                                                                 |
| R1.8c        | [POST] `/login`        | User with password with no lowercase characters cannot log in and error message is displayed.                                                                 |
| R1.8d        | [POST] `/login`        | User with password with no special characters cannot log in and error message is displayed.                                                                   |
| R1.9         | [POST] `/login`        | For any formatting errors, render the login page and show the message 'email/password format is incorrect                                                     |
| R1.10        | [POST] `/login`        | If email/password are correct, redirect to `/`                                                                                                                |
| R1.11        | [POST] `/login`        | Otherwise, redirect to `/login` and show message 'email/password combination incorrect'                                                                       |
| R1.11a       | [POST] `/login`        | Invalid email redirects to `/login` with error message                                                                                                        |
| R1.11b       | [POST] `/login`        | Invalid password redirects to `/login` with error message.                                                                                                    |
| R2.1         | [GET] `/register`      | If the user has logged in, redirect back to the user profile page                                                                                             |
| R2.2         | [GET] `/register`      | otherwise, show the user registration page                                                                                                                    |
| R2.3         | [GET] `/register`      | the registration page shows a registration form requesting: email, user name, password, password2                                                             |
| R2.4         | [POST] `/register`     | The registration form can be submitted as a POST request to the current URL (/register)                                                                       |
| R2.5         | [POST] `/register`     | Email, password, password2 all have to satisfy the same required as defined in R1                                                                             |
| R2.5a        | [POST] `/register`     | Email cannot be empty                                                                                                                                         |
| R2.5b        | [POST] `/register`     | Password cannot be empty                                                                                                                                      |
| R2.5c        | [POST] `/register`     | Password2 cannot be empty                                                                                                                                     |
| R2.5d        | [POST] `/register`     | Email has to follow addr-spec defined in RFC 5322                                                                                                             |
| R2.5e        | [POST] `/register`     | Password has to meet the required complexity: minimum length 6                                                                                                |
| R2.5f        | [POST] `/register`     | Password has to meet the required complexity: at least one upper case                                                                                         |
| R2.5g        | [POST] `/register`     | Password has to meet the required complexity: least one lower case                                                                                            |
| R2.5h        | [POST] `/register`     | Password has to meet the required complexity: at least one special character                                                                                  |
| R2.6         | [POST] `/register`     | Password and password2 have to be exactly the same                                                                                                            |
| R2.7         | [POST] `/register`     | Username has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.                                         |
| R2.7a        | [POST] `/register`     | Username has to be non-empty.                                                                                                                                 |
| R2.7b        | [POST] `/register`     | Username has to be alphanumeric-only.                                                                                                                         |
| R2.7c        | [POST] `/register`     | Username is not allowed if the first character is space.                                                                                                      |
| R2.7d        | [POST] `/register`     | Username is not allowed if the last character is space.                                                                                                       |
| R2.8         | [POST] `/register`     | User name has to be longer than 2 characters and less than 20 characters.                                                                                     |
| R2.8a        | [POST] `/register`     | User name has to be longer than 2 characters.                                                                                                                 |
| R2.8b        | [POST] `/register`     | User name has to be less than 20 characters.                                                                                                                  |
| R2.9         | [POST] `/register`     | For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)                             |
| R2.10        | [POST] `/register`     | If the email already exists, show message 'this email has been ALREADY used'                                                                                  |
| R2.11        | [POST] `/register`     | If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page                        |
| R3.1         | [GET] `/`              | If the user hasn't logged in, redirect the login page                                                                                                         |
| R3.2         | [GET] `/`              | This page shows a header 'Hi {}'.format(user.name)                                                                                                            |
| R3.3         | [GET] `/`              | This page shows user balance.                                                                                                                                 |
| R3.4         | [GET] `/`              | This page shows a logout link, pointing to /logout                                                                                                            |
| R3.5         | [GET] `/`              | This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. |
| R3.6         | [GET] `/`              | This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date.                                        |
| R3.7         | [GET] `/`              | This page contains a form that a user can buy new tickets. Fields: name, quantity                                                                             |
| R3.8         | [GET] `/`              | This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date                                             |
| R3.9         | [GET] `/`              | The ticket-selling form can be posted to /sell                                                                                                                |
| R3.10        | [GET] `/`              | The ticket-buying form can be posted to /buy                                                                                                                  |
| R3.11        | [GET] `/`              | The ticket-update form can be posted to /update                                                                                                               |
| R4.1         | [POST] `/sell`         | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character                                       |
| R4.1a        | [POST] `/sell`         | Ticket name with special characters produces an error message.                                                                                                |
| R4.1b        | [POST] `/sell`         | Ticket name with leading space produces an error message.                                                                                                     |
| R4.1c        | [POST] `/sell`         | Ticket name with trailing space produces an error message.                                                                                                    |
| R4.2         | [POST] `/sell`         | The name of the ticket is no longer than 60 characters                                                                                                        |
| R4.3         | [POST] `/sell`         | The quantity of the tickets has to be more than 0, and less than or equal to 100                                                                              |
| R4.3a        | [POST] `/sell`         | Ticket quantity of 0 or less produces an error message.                                                                                                       |
| R4.3b        | [POST] `/sell`         | Ticket quantity of over 100 produces an error message.                                                                                                        |
| R4.4         | [POST] `/sell`         | Price has to be of range [10, 100]                                                                                                                            |
| R4.4a        | [POST] `/sell`         | Price of less than 10 produces an error message.                                                                                                              |
| R4.4b        | [POST] `/sell`         | Price of greater than 100 produces an error message.                                                                                                          |
| R4.5         | [POST] `/sell`         | Date must be given in the format YYYYMMDD (e.g. 20200901)                                                                                                     |
| R4.5a        | [POST] `/sell`         | Mis-formatted date produces error message.                                                                                                                    |
| R4.5b        | [POST] `/sell`         | Date in the past produces error message.                                                                                                                      |
| R4.6         | [POST] `/sell`         | For any errors, redirect back to / and show an error message                                                                                                  |
| R4.7         | [POST] `/sell`         | The added new ticket information will be posted on the user profile page                                                                                      |
| R5.1         | [POST] `/update`       | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.                                      |
| R5.1a        | [POST] `/update`       | The name of the ticket must be alphanumeric-only.                                                                                                             |
| R5.1b        | [POST] `/update`       | The name of the ticket is not allowed if the first character is a space.                                                                                      |
| R5.1c        | [POST] `/update`       | The name of the ticket is not allowed if the last character is a space.                                                                                       |
| R5.2         | [POST] `/update`       | The name of the ticket is no longer than 60 characters                                                                                                        |
| R5.3         | [POST] `/update`       | The quantity of the tickets has to be more than 0, and less than or equal to 100.                                                                             |
| R5.3a        | [POST] `/update`       | The quantity of the tickets has to be more than 0.                                                                                                            |
| R5.3b        | [POST] `/update`       | The quantity of the tickets has to be less than or equal to 100.                                                                                              |
| R5.4         | [POST] `/update`       | Price has to be of range [10, 100]                                                                                                                            |
| R5.4a        | [POST] `/update`       | Price has to be greater than or equal to 10.                                                                                                                  |
| R5.4b        | [POST] `/update`       | Price has to be less than or equal to 100.                                                                                                                    |
| R5.5         | [POST] `/update`       | Date must be given in the format YYYYMMDD (e.g. 20200901)                                                                                                     |
| R5.5a        | [POST] `/update`       | Year must be formatted properly.                                                                                                                              |
| R5.5b        | [POST] `/update`       | Month must be formatted properly.                                                                                                                             |
| R5.5c        | [POST] `/update`       | Day must be formatted properly.                                                                                                                               |
| R5.5d        | [POST] `/update`       | Date must not have passed.                                                                                                                                    |
| R5.6         | [POST] `/update`       | The ticket of the given name must exist                                                                                                                       |
| R5.7         | [POST] `/update`       | For any errors, redirect back to / and show an error message                                                                                                  |
| R5.7a        | [POST] `/update`       | An update with an error displays an error message                                                                                                             |
| R5.7b        | [POST] `/update`       | An update without errors passes successfully                                                                                                                  |
| R6.1         | [POST] `/buy`          | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.                                      |
| R6.1a        | [POST] `/buy`          | Ticket name with special characters produces an error message.                                                                                                |
| R6.1b        | [POST] `/buy`          | Ticket name with leading space produces an error message.                                                                                                     |
| R6.1c        | [POST] `/buy`          | Ticket name with trailing space produces an error message.                                                                                                    |
| R6.2         | [POST] `/buy`          | The name of the ticket is no longer than 60 characters                                                                                                        |
| R6.3         | [POST] `/buy`          | The quantity of the tickets has to be more than 0, and less than or equal to 100                                                                              |
| R6.3a        | [POST] `/buy`          | Ticket quantity of 0 or less produces an error message.                                                                                                       |
| R6.3b        | [POST] `/buy`          | Ticket quantity of over 100 produces an error message.                                                                                                        |
| R6.4a        | [POST] `/buy`          | The ticket name exists in the database and the quantity is more than the quantity requested to buy(positive).                                                 |
| R6.4b        | [POST] `/buy`          | The ticket name exists in the database and the quantity is less than the quantity requested to buy(negative).                                                 |
| R6.4c        | [POST] `/buy`          | The ticket does not exists in the database and the quantity is more than the quantity requested to buy(negative).                                             |
| R6.5a        | [POST] `/buy`          | The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)(positive).                                                          |
| R6.5b        | [POST] `/buy`          | The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)(negative).                                                          |
| R6.6         | [POST] `/buy`          | For any errors, redirect back to / and show an error message                                                                                                  |
| R7.1         | [GET,POST] `/logout`   | Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.                  |
| R7.1a        | [GET,POST] `/logout`   | Basic logout invalidates the current session check                                                                                                            |
| R7.1b        | [GET,POST] `/logout`   | Advanced logout invalidates the current session check                                                                                                         |
| R7.1c        | [GET,POST] `/logout`   | After logout user can't access restricted pages                                                                                                               |
| R8.1         | [any] `/*`             | For any other requests except the ones above, the system should return a 404 error                                                                            |
| R8.1a        | [any] `/*`             | When not logged in return a 404 error for any other requests except the authorized ones                                                                       |
| R8.1b        | [any] `/*`             | When logged in return a 404 error for any other requests except the authorized ones                                                                           |
| R8.1c        | [any] `/*`             | When not logged in ensure a 404 error is not sent for the authorized requests                                                                                 |
| R8.1d        | [any] `/*`             | When logged in ensure a 404 error is not sent for the authorized requests                                                                                     |

# Test Plan

**How did your team organize the documentations of the test cases (e.g. where did you store the test case markdown file for each team member).**  
To organize the documentations, we created a separate markdown file for each page/route for a total of 8 different markdown files. 
This was done because it made finding test cases that affect the same area far easier then splitting then by group member, while also keeping the GET and POST cases that some pages have together.

**Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.**  
To test the frontend, the backend functions are mocked using a fake test object where for a given input, some expected output is returned. 
This allows for the frontend pages and methods to be unit tested in isolation to the backend, without using a browser. 
In contrast, integration testing of the frontend and backend together is done against an automated browser using Selenium and a mocked backend server. 
Selenium interacts with the frontend to verify the correct backend behaviour.  
All tests are run on GitHub whenever a commit is pushed to remote. 
For each commit, the dependencies are installed and the changes are linted before all unit and integration tests are run.

**How are you going to organize different test case code files? (a folder for a specification?)**  
In a similar vein to what we did for the test cases’ documentation, the test case code files will be stored in separate folders for each page/route.