from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS, cross_origin
from models import Question
from exceptions import ParsingError

quizzes_routes = Blueprint('quizzes_routes', __name__)

@quizzes_routes.route('/quizzes', methods=['Post'])
@cross_origin()
def post_quiz():
    try:
        data = request.get_json()
        category=data.get('quiz_category')
        previous_questions=data.get('previous_questions')
        try:
            dict(category) and int(category['id'])
        except Exception as err:
            print(f'error parsing for post quiz: {err}') 
            raise ParsingError(message='Unable to parse')
        # if a previous question was entered, which is optional, we want to ensure that all items are ints
        if previous_questions:
            try:
                list(previous_questions)
                for question in previous_questions:
                    int(question)
            except Exception as err:
                print(f'error parsing for post quiz: {err}') 
                raise ParsingError(message='Unable to parse')
        # if no previous question, model method will just get any question of cat
        next_question=Question.get_next_question(self=Question, cid=category['id'], previous_questions=previous_questions)
        return jsonify({
            'success': True,
            'next_question':next_question
        })
    except ParsingError as err:
        abort(422, description='Not all values are in the correct type. Please check the documentation')
    except Exception as err:
        print(f'error posting quiz: {err}')
        abort(400, description='Not all of the required data was received')