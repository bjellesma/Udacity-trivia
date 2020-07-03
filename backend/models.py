import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from secure import (
    CONNECT_STRING, DEBUG, TEST_CONNECT_STRING
)
import random

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=CONNECT_STRING):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String)
  answer = Column(String)
  category = Column(String)
  difficulty = Column(Integer)

  def __init__(self, question, answer, category, difficulty):
    self.question = question
    self.answer = answer
    self.category = category
    self.difficulty = difficulty

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def search(self, search_term):
    return Question.query.with_entities(Question.id, 
                                      Question.question, 
                                      Question.answer, 
                                      Question.difficulty, 
                                      Question.category).filter(
                                        Question.question.ilike(f'%{search_term}%')
                                      ).all()

  def get_next_question(self, cid, previous_questions=None):
    questions_list = []
    # if cat id was zero, return any question
    if cid == 0:
      questions = Question.query.all()
    # if no question id was entered, simplify the query to only filter by category
    elif not previous_questions:
      questions = Question.query.filter(Question.category==cid).all()
    else:
      questions = Question.query.filter(db.and_(Question.category==cid, Question.id.notin_(previous_questions))).all()
    for question in questions:
      questions_list.append(question.id)
    if questions_list:
      next_question = Question.query.get(random.choice(questions_list))
      next_question = {
      'id': next_question.id,
      'question': next_question.question,
      'answer': next_question.answer,
      'difficulty': next_question.difficulty,
      'category': next_question.category
    }
    else:
      next_question = False
    
    return next_question

  def get_questions_in_cat(self, cid):
    questions = Question.query.filter(Question.category==cid).count()
    return questions

  def format(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category,
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }