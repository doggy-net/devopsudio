from celery import Celery
from celery.result import AsyncResult
from flask import Flask, jsonify, render_template, url_for

from devopstudio.config import MQConfig


mq_config = MQConfig()
amqp_conn_str = mq_config.get_conn_str()

app = Flask(__name__,
            static_folder='dist',
            static_url_path='',
            template_folder='dist')
app.config.update(
    CELERY_BROKER_URL=amqp_conn_str,
    CELERY_RESULT_BACKEND=amqp_conn_str
)

celeryapp = Celery(app.name,
                   broker=app.config['CELERY_BROKER_URL'],
                   backend=app.config['CELERY_RESULT_BACKEND'])


@app.route('/')
def index():
    return render_template("index.html")


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("index.html")


@celeryapp.task()
def long_task_add(a, b):
    return a + b


@app.route('/test')
def test():
    return jsonify({'aaa': 'test'})


@app.route('/longtask', methods=['POST'])
def longtask():
    task = long_task_add.delay(1, 2)
    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    print(task_id)
    task = AsyncResult(task_id, app=celeryapp)
    print('synced', task.get())
    # if task.state == 'PENDING':
    #     response = {
    #         'state': task.state,
    #         'current': 0,
    #         'total': 1,
    #         'status': 'Pending...'
    #     }
    # elif task.state != 'FAILURE':
    #     response = {
    #         'state': task.state,
    #         'current': task.info.get('current', 0),
    #         'total': task.info.get('total', 1),
    #         'status': task.info.get('status', '')
    #     }
    #     if 'result' in task.info:
    #         response['result'] = task.info['result']
    # else:
    #     # something went wrong in the background job
    #     response = {
    #         'state': task.state,
    #         'current': 1,
    #         'total': 1,
    #         'status': str(task.info),  # this is the exception raised
    #         'result': task.get(),
    #     }
    return jsonify({'result': task.get()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
