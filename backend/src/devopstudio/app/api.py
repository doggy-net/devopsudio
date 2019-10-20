from celery.result import AsyncResult
from flask import abort, Blueprint, jsonify, make_response, request

from devopstudio.db import models
from devopstudio.worker import app as celeryapp, tasks


bp = Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/discovery', methods=('GET', 'POST', 'DELETE'))
def discover():
    if request.method == 'POST':
        data = request.get_json()
        task = tasks.discover.delay(data['ips'])
        if task:
            discovery_task = models.OneInstanceTask(
                name='discovery',
                task_id=task.id)
            discovery_task.save()
            return jsonify({'taskId': task.id}), 202
        else:
            return abort(500)
    elif request.method == 'DELETE':
        discovery_task = models.OneInstanceTask.objects.get(
            {'_id': 'discovery'})
        celeryapp.control.revoke(discovery_task.task_id, terminate=True)
        return '', 204
    elif request.method == 'GET':
        discovery_task = models.OneInstanceTask.objects.get(
            {'_id': 'discovery'})
        result = AsyncResult(discovery_task.task_id, app=celeryapp)
        if result.successful():
            return jsonify({
                'state': result.state,
                'progress': result.info.get('total'),
                'total': result.info.get('total'),
            })
        elif result.failed():
            return jsonify({
                'state': result.state,
                'progress': result.info.get('total'),
                'total': result.info.get('total'),
            })
        else:
            progress, total = (result.info.get('progress', 0), result.info.get('total', 100)) \
                if result.info else (0, 100)
            return jsonify({
                'state': result.state,
                'progress': progress,
                'total': total,
            }), 202
    return abort(404)
