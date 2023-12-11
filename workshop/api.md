## List of prompt to generate code
* REST API
* Working with database
* Refactoring code
* Explain code
* Testing
  * Design test case
  * Write unit test and api test
* Deployment with Docker

### Step 1 
```
Role Golang developer,
I want to generate RESTful API with Go and Gin framework from my requirement from below

"""
Create a new user
* first name
* last name
* age


POST /users
Request body
{
    "first_name": "somkiat",
    "last_name": "pui",
    "age": 40
}

Response for API

200 => success
{
    "id": 1,
    "first_name": "Somkiat",
    "last_name": "Pui",
    "age": 40
}

409 => First name is duplicated
{
    "message": "First name is duplicated"
}

500 => Internal server error
{
    "message": "Internal server error"
}
"""

```

### Step 2 :: More tasks
* Generate code to insert a new user in MySQL database
* Refactor code :: try to move code from controller to service layer
* In database layer or repository layer, try to generate code to check for duplicate first name in the database
* Refactor code, move code from main() function to Controller layer, eg. UserController
* Generate table scheman and diagram
  * Try to generate database diagram of user table in markdown format
  * Try to generate database diagram of user table in DBML format
  * Try to generate sql query to create table user

### Step 3 :: Testing
* As a Tester/QA to test software, i want to generate test cases for REST API 
- success case
- failure case
- edge case
* As a Tester/QA to test software, i want to generate test cases for REST API with table format (markdown) 
- success case
- failure case
- edge case

* As a Go developer, i want to generate API test with testing package and testify package
- success case
- failure case
- edge case