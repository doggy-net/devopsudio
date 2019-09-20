from flask import abort, Blueprint, jsonify, render_template, request


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.app_errorhandler(404)
def page_not_found(e):
    if request.path.startswith('/api/'):
        return jsonify({"message": "API not found"}), 404
    return render_template('index.html')
