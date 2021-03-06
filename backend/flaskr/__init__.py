import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# route imports
from routes.questions import questions_routes
from routes.categories import categories_routes
from routes.quizzes import quizzes_routes
from models import setup_db


QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  
  setup_db(app)
  # This Cors protection will allow all domains to access these endpoints
  # Necessary because our frontend connects with a different port
  CORS(app, resources={r"/api/*": {"origins": "*"}}) 
  app.register_blueprint(questions_routes)
  app.register_blueprint(categories_routes)
  app.register_blueprint(quizzes_routes)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  @app.errorhandler(400)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "Bad Request",
      "additional_information": error.description
      }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "Not Found",
      "additional_information": error.description
    }), 404

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "Method not allowed",
      "additional_information": error.description
      }), 405

  @app.errorhandler(422)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "Unable to process",
      "additional_information": error.description
      }), 422

  @app.errorhandler(500)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "Internal Server Error",
      "additional_information": error.description
      }), 500
  
  @app.route('/', methods=['GET'])
  def get_index():
    """Returns a message to tell the user that they've successfully connected"""
    return jsonify({
      'success': True,
      'message': 'Hello API'
    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    