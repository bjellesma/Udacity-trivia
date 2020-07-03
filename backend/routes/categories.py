from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS, cross_origin
from models import Category

categories_routes = Blueprint('categories_routes', __name__)
CATEGORIES_PER_PAGE = 10

@categories_routes.route('/api/categories')
@cross_origin()
def get_categories():
    try:
        page = int(request.args.get('page', 1))
    except:
        abort(422, description="The query parameters were sent in the wrong format. Check the Documentation.")
    start = (page - 1) * CATEGORIES_PER_PAGE
    end = start + CATEGORIES_PER_PAGE
    categories = Category.query.all()

    total_categories = [category.format() for category in categories]
    if not total_categories:
        abort(404, description='There are no categories')
    formatted_categories = total_categories[start:end]
    if len(formatted_categories) == 0:
        abort(404, description='Page out of range')
    return jsonify({
        'success': True,
        'categories': formatted_categories,
        'total_categories': len(total_categories)
    })

