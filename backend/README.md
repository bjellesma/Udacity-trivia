# Full Stack Trivia API Backend

## Getting Started

### Dependencies

1. Download and install [Python](https://www.python.org/downloads/) if it is not already available on your system
2. `pipenv` is used as the virtual environment of choice for this application and you can install it using `pip install pipenv`
3. Install [NodeJS](https://nodejs.org/en/download/) in order to run the development scripts (nodejs is also planned to be used for the frontend)
2. Create a database from your database installation for use in the app
    1. In Postgresql, for example, you can install a local database with `createdb trivia` and test database with `createdb trivia_test`
    2. Run `psql trivia < trivia.psql` to install the initial questions and categories to the database

### Install the project

0. Clone this project to your machine.

1. From the command line, navigate to the root directory, `trivia_api`.

2. Edit `.env-template` and fill in the information to connect to the database of your choice
    1. Rename the file as `.env` so that it will be recognized by the app
    
    *Note*: This app has only been tested using postgres
The following is the schema as well as the expected data for the `.env` file
```
DATABASE_TYPE=The type of database that the user has created. This app has only been tested with postgresql
DATABASE_HOST=LEAVE THIS VALUE AS localhost!
DATABASE_PORT=port number that the database runs on
DATABASE_USER=username of user that has access to the database created by the user
DATABASE_PASSWORD=password for the database. Leave lank if no password is set
DATABASE_DATABASE=LEAVE THIS VALUE AS trivia!
TEST_DATABASE=LEAVE THIS VALUE AS trivia_test!
DEBUG=Boolean. If true, the app will run in debug so that it can host reload
```
The following is an example of a complete `.env` file:
```
DATABASE_TYPE=postgresql
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_DATABASE=trivia
TEST_DATABASE=trivia_test
DEBUG=True
```

3. Run `pipenv install` to install the virtual environment
    1. This command will also install the backend packages located inside of `pipfile`

4. Navigate to the `/backend` directory on the command line.

5. Run `npm run server` to start the development server.

6. Open a webbrowser and ensure that you can connect to [http://localhost:5000](http://localhost:5000)
    1. You should be greeted with a welcome message saying "Hello API"

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

# Contributing

1. Fork this repository

2. Use the instructions to set up a local development server
    1. Use the api documentation for more information on how to make requests to the endpoints.

3. Once you've made any modifications using the Code Style Guide listed in the next section, run the code through unit tests using `npm run test`.
    1. If you've written any new endpoints, please also write a new unit test for the endpoint.
    2. Please also pay attention to the code coverage as output and ensure that coverage is at least 80%
4. When your code is passing the unit tests, please submit a pull request

# Code Style Guide

This code abides by [PEP8](https://www.python.org/dev/peps/pep-0008/) with the exception of using tabs over any spaces.

# Credits

* Bill Jellesma
* Udacity - Udacity created the idea for the course as a teaching project

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. `/quizzes`

Here is the original documentation: [https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter/backend](https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter/backend)

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```
