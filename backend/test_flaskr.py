import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from secure import TEST_CONNECT_STRING
from flaskr import create_app
from models import setup_db, Question, Category

# headers is global since we need it for both classes
headers = {'Content-Type': 'application/json'}

class QuizTestCast(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        self.quiz_next_question = {
            'quiz_category': {
                'type': 'Art',
                'id': 2
            },
            'previous_questions':[
                2
            ]
        }
        self.quiz_next_question_noquestion = {
            'quiz_category': {
                'type': 'Art',
                'id': 2
            }
        }
        self.quiz_next_question_422 = {
            'quiz_category': {
                'type': 'Art',
                'id': 2
            },
            'previous_questions':[
                'adafd'
            ]
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_quizzes(self):
        res = self.client().post('/quizzes',
                                data=json.dumps(self.quiz_next_question),
                                headers=headers
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # Just test true for a random question since we can't get the question
        self.assertTrue(data['next_question'])

    def test_quizzes_422(self):
        res = self.client().post('/quizzes',
                                data=json.dumps(self.quiz_next_question_422),
                                headers=headers
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], 'Not all values are in the correct type. Please check the documentation')

    def test_quizzes_noquestion(self):
        res = self.client().post('/quizzes',
                                data=json.dumps(self.quiz_next_question_noquestion),
                                headers=headers
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # Just test true for a random question since we can't get the question
        self.assertTrue(data['next_question'])
        

class QuestionTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        self.new_question = {
            'question': 'Who is the Alanis Morissette song "You Outta Know" about?',
            'answer': 'Uncle Joey',
            'difficulty': 2,
            'category': 5
        }
        # Notice the string where an int should be
        self.new_question_error = {
            'question': 'What is my favorite color?',
            'answer': 'Blue',
            'difficulty': 'five',
            'category': 5
        }
        self.new_question_blank = {
            'question': 'adfafd',
            'answer': 'afdasfd',
            'difficulty': 0,
            'category': 0
        }
        self.search_questions = {
            'search_term': 'movie',
            'questions': [
                {
                    'question_id': 2,
                    'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?',
                    'answer': 'Apollo 13',
                    'difficulty': 4,
                    'category': 5
                }
            ]
        }
        self.search_questions_error = {
            'search_term': 'adfas',
            'questions': []
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_index(self):
        """
        test for success on homepage
        """
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Hello API')

    def test_get_questions(self):
        """
        return list of questions pagenated 10 per page
        """
        res = self.client().get('/api/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # assert true will ensure that a nonzero value is returned
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_get_questions_422(self):
        """
        test that sending page in the wrong format yields a 422 error
        """
        res = self.client().get('/api/questions?page=afda')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], "The query parameters were sent in the wrong format. Check the Documentation.")

    def test_get_questions_page_error(self):
        """test that sending a page that doesnt exist will properly yield a 404"""
        res = self.client().get('/api/questions?page=10')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], 'Page out of range')

    def test_get_questions_of_category(self):
        """test getting questions of a certain category"""
        res = self.client().get('/api/categories/2/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # assert true will ensure that a nonzero value is returned
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], 2)

    def test_get_questions_of_category_error(self):
        """test getting questions of a certain category"""
        res = self.client().get('/api/categories/12/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # assert true will ensure that a nonzero value is returned
        self.assertTrue(data['additional_information'], 'Category out of range')

    def test_create_question(self):
        """test that users are able to create a question"""
        res = self.client().post('/api/questions',
                                data=json.dumps(self.new_question),
                                headers=headers
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_question_error(self):
        """test that users are not able to creat a question without the correct data types"""
        res = self.client().post('/api/questions',
                                data=json.dumps(self.new_question_error),
                                headers=headers
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], 'Not all values are in the correct type. Please check the documentation')

    def test_create_question_blank(self):
        """test creating a blank question"""
        res = self.client().post('/api/questions',
                                data=json.dumps(self.new_question_blank),
                                headers=headers
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], 'Not all values are in the correct type. Please check the documentation')

    def test_delete_question(self):
        """test that the user can successfully delete a question"""
        res = self.client().delete('/api/questions/5')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Question successfully deleted')
        self.assertEqual(data['question_id'], 5)

    def test_delete_question_error(self):
        """test that the user receives a 404 when enterring an invalid id"""
        res = self.client().delete('/api/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], 'Question out of range')

    def test_search_questions(self):
        """test using the search functionality"""
        res = self.client().post(f'/api/search/questions/{self.search_questions["search_term"]}')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['questions'], self.search_questions['questions'])

    def test_search_questions_error(self):
        """test using the search functionality. String with No Results"""
        res = self.client().post(f'/api/search/questions/{self.search_questions_error["search_term"]}')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['questions'], self.search_questions_error['questions'])


class CategoryTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_categories(self):
        """
        return list of categories
        """
        res = self.client().get('/api/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_categories'])

    def test_get_categories_422(self):
        """
        test that sending page in the wrong format yields a 422 error
        """
        res = self.client().get('/api/categories?page=afda')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], "The query parameters were sent in the wrong format. Check the Documentation.")

    def test_get_categories_page_error(self):
        """test that sending a page that doesnt exist will properly yield a 404"""
        res = self.client().get('/api/categories?page=10')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['additional_information'], 'Page out of range')

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()