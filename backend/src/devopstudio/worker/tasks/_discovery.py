import time
from celery import current_task

from devopstudio.plugins.driver import Selector
from devopstudio.plugins.driver.cli import ios


def discover_one_ip(ip_addr):
    test_selector = Selector([{'condition': '*', 'driver': ios.DriverModule}])
    ipstr = str(ip_addr)
    matched_driver = test_selector.match(ipstr)
    if matched_driver:
        device = matched_driver(ipstr)
        device.parsing()
        # print(device.execute_command('show version'))


def update_progress(task, progress, total, step=1):
    if progress % step == 0:
        task.update_state(
            state='PROGRESSING', meta={'progress': progress, 'total': total})
