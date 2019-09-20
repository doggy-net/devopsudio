from celery.result import AsyncResult
from flask import abort, Blueprint, jsonify, make_response, request

from devopstudio.worker import app as celeryapp, tasks


bp = Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/discovery', methods=('GET', 'POST', 'DELETE'))
def discover():
    if request.method == 'POST':
        data = request.get_json()
        task = tasks.discovery.delay(data['ips'])
        if task:
            res = make_response(jsonify({'taskId': task.id}), 202)
            res.headers['Retry-After'] = 10
            return res
        else:
            return abort(500)
    elif request.method == 'GET':
        task_id = request.args.get('taskId')
        if not task_id:
            return abort(404)
        result = AsyncResult(task_id, app=celeryapp)
        if result.ready():
            return jsonify({'result': result.get()})
        else:
            print(result.state, result.info)
            return jsonify({'result': 'doing'}), 202
    elif request.method == 'DELETE':
        pass
    return abort(404)
