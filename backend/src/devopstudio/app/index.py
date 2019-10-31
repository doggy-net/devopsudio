from flask import abort, Blueprint, jsonify, render_template, request, send_file


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/icons/<icon_name>')
def icon(icon_name):
    return send_file('icons/' + icon_name)


@bp.app_errorhandler(404)
def page_not_found(e):
    if request.path.startswith('/api/'):
        return jsonify({"message": "API not found"}), 404
    elif request.path.startswith('/icon/'):
        return jsonify({"message": "ICON not found"}), 404
    return render_template('index.html')
