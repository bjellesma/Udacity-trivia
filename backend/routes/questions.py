from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS, cross_origin
from models import Question, Category
from exceptions import ParsingError

questions_routes = Blueprint('questions_routes', __name__)
QUESTIONS_PER_PAGE = 10

@questions_routes.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

@questions_routes.route('/api/questions', methods=['GET'])
@cross_origin()
def get_questions():
    try:
        page = int(request.args.get('page', 1))
    except:
        abort(422, description="The query parameters were sent in the wrong format. Check the Documentation.")
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = Question.query.all()
    categories = Category.query.all()
    total_categories = [category.format() for category in categories]
    for category in total_categories:
        print(f'cat: {category}')
    total_questions = [question.format() for question in questions]
    if not total_questions:
        abort(404, description='There are no questions')
    formatted_questions = total_questions[start:end]
    # if a page was used that doesn't have any questions
    if len(formatted_questions) == 0:
        abort(404, description='Page out of range')
    return jsonify({
        'success': True,
        'questions': formatted_questions,
        'categories': {category['id']: category['type'] for category in total_categories},
        'total_questions': len(total_questions)
    })

@questions_routes.route('/api/questions', methods=['POST'])
@cross_origin()
def create_question():
    try:
        data = request.get_json()
        question = data.get('question')
        answer = data.get('answer')
        difficulty = data.get('difficulty')
        category = data.get('category')
        # If any params are missing, we'll abort to a 422
        if not question or not answer or not difficulty or not category:
            raise ParsingError(message='Unable to parse')
        try:
            int(difficulty) and int(category)
        except Exception as err:
            print(f'error parsing for create_question: {err}') 
            raise ParsingError(message='Unable to parse')
        # Test if the difficulty and category are 0 when converted
        if int(difficulty) == 0 or int(category) == 0:
            raise ParsingError(message='Unable to parse')
        question = Question(
            question=question,
            answer=answer,
            category=category,
            difficulty=difficulty
        )
        Question.insert(question)
        return jsonify({
            'success': True,
            'question_id': question.id 
        })
    except ParsingError as err:
        abort(422, description='Not all values are in the correct type. Please check the documentation')
    except Exception as err:
        print(f'error posting question: {err}')
        abort(400, description='Not all of the required data was received')

@questions_routes.route('/api/questions/<int:question_id>', methods=['DELETE'])
@cross_origin()
def delete_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        abort(404, description="Question out of range")
    Question.delete(question)
    return jsonify({
        "success": True,
        "message": "Question successfully deleted",
        "question_id": question_id 
    })

@questions_routes.route('/api/categories/<int:category_id>/questions')
@cross_origin()
def get_questions_of_category(category_id):
    """get questions of a certain category"""
    questions = Question.query.filter(Question.category==category_id).all()
    if len(questions) == 0:
        abort(404, description='Category out of range')
    return jsonify({
        'success': True,
        'total_questions': len(questions),
        'current_category': category_id
    })

@questions_routes.route('/api/search/questions/<search_term>', methods=['POST'])
@cross_origin()
def post_search_questions(search_term):
    questions_list = []
    questions = Question.search(self=Question, search_term=search_term)
    for question in questions:
        questions_list.append({
            'question_id': question.id,
            'question': question.question,
            "answer": question.answer,
            "difficulty": question.difficulty,
            "category": question.category
        })
    return jsonify({
        "success":True,
        "questions": questions_list
    })