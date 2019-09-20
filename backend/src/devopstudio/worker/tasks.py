import time
from celery import current_task

from devopstudio.worker import app
from devopstudio.worker.live import cli


@app.task()
def discovery(ip_list):
    if isinstance(ip_list, list):
        pass
    elif isinstance(ip_list, str):
        pass
    else:
        raise TypeError('invalid ip_list type')
    # current_task.update_state(
    #     state='PROGRESSING', meta={'current': i, 'total': 100})
    # with cli.TelnetSession(ip_list) as ts:
    #     ts.update_cfg({
    #         'username': 'admin',
    #         'password': 'pwdadmin',
    #         'enable': 'enadmin',
    #     })
    #     return ts.execute('show run')
