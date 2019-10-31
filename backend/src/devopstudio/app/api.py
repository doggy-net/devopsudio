from celery import chain, group
from celery.result import AsyncResult
from flask import abort, Blueprint, jsonify, make_response, request

from devopstudio.db import models
from devopstudio.worker import app as celeryapp, tasks


bp = Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/discovery', methods=('GET', 'POST', 'DELETE'))
def discover():
    if request.method == 'POST':
        data = request.get_json()
        task_group = tasks.discover.si(data['ips']) | tasks.build_explorers.si()
        task_result = task_group.apply_async()
        if task_result:
            discovery_task = models.OneInstanceTask(
                name='discovery',
                task_id=task_result.parent.id)
            discovery_task.save()
            return jsonify({'taskId': task_result.parent.id}), 202
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


@bp.route('/explorers')
def explorer():
    if request.args and 'name' in request.args:
        try:
            explorer = models.Explorer.objects.get({'_id': request.args['name']})
            return jsonify(explorer.to_son())
        except:
            return abort(404)
    explorers = models.Explorer.objects.all()
    explorer_names = [explorer.name for explorer in explorers]
    result = {
        'explorers': explorer_names,
        'default': explorers[0].to_son() if explorers else None
    }
    return jsonify(result)
