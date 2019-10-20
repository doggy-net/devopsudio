import time
from celery import current_task

from devopstudio.db import models
from devopstudio.worker import app
# from devopstudio.worker.live import cli


@app.task()
def discovery(ip_list):
    if isinstance(ip_list, list):
        pass
    elif isinstance(ip_list, str):
        pass
    else:
        raise TypeError('invalid ip_list type')
    for i in range(10):
        time.sleep(3)
        current_task.update_state(
            state='PROGRESSING', meta={'progress': i, 'total': 10})
    return {'progress': 10, 'total': 10}
