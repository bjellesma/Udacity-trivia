# Full Stack API Final Project



## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)


# Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

# Getting Started

## Dependencies

0. `pipenv` is used as the virtual environment of choice for this application and you can install it using `pip install pipenv`
1. Install [NodeJS](https://nodejs.org/en/download/) in order to run the development scripts (nodejs is also planned to be used for the frontend)
2. Local installation of a database such as [postgres](https://www.postgresql.org/download/)
3. Create a database from your database installation for use in the app
    1. In Postgresql, for example, you can install a localdatabase with `createdb <database_name>` where `database_name` is any name you choose.

*Hint: To create a database on linux systems, you may need to use `sudo -u postgres -i` to temporarily switch to the postgres user*

## Install the project

**At this time, install the project is the same as installing the local environment.**

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
DATABASE_DATABASE=The name of the database that the user created to store the book data
TEST_DATABASE=The name of the database that the user created for the app to run through tests
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
TEST_DATABASE=test_bookshelf
DEBUG=True
```

3. Run `pipenv install` to install the virtual environment
    1. This command will also install the backend packages located inside of `pipfile`

4. Navigate to the `/backend` directory on the command line.

5. Run `npm run server` to start the development server.

6. Open a webbrowser and ensure that you can connect to [http://localhost:5000](http://localhost:5000)

# Contributing

**Docs on the api can be found [here](./backend/api_reference.md)

1. Fork this repository

2. Use the instructions to set up a local development server
    1. Use the api documentation for more information on how to make requests to the endpoints.

3. Once you've made any modifications using the Code Style Guide listed in the next section, run the code through unit tests using npm run test.
    1. If you've written any new endpoints, please also write a new unit test for the endpoint.
4. When your code is passing the unit tests, please submit a pull request

# Code Style Guide

This code abides by [PEP8](https://www.python.org/dev/peps/pep-0008/) with the exception of using tabs over any spaces.

# Credits

* Bill Jellesma
* Udacity - Udacity created the idea for the course as a teaching project

