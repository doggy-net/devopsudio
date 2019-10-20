from celery import current_task
from netaddr import IPAddress, IPNetwork, IPRange

from . import _discovery
from devopstudio.worker import app
from devopstudio.plugins.explorer import object_type


@app.task()
def discover(ip_list):
    if not isinstance(ip_list, str):
        raise TypeError('invalid ip_list type')
    ip_list = ip_list.split(';')
    to_do_list = []
    done_set = set()
    total = 0
    progress = 0
    for ip_item in ip_list:
        if '-' in ip_item:
            ip_range = IPRange(*ip_item.split('-'))
            to_do_list.append(ip_range)
            total += len(ip_range)
        elif '/' in ip_item:
            ip_network = IPNetwork(ip_item)
            to_do_list.append(ip_network)
            total += len(ip_network)
        else:
            ip_address = IPAddress(ip_item)
            to_do_list.append(ip_address)
            total += 1
    for ip_obj in to_do_list:
        if isinstance(ip_obj, (IPRange, IPNetwork)):
            for ip_addr in ip_obj:
                if ip_addr in done_set:
                    continue
                _discovery.discover_one_ip(ip_addr)
                done_set.add(ip_addr)
                progress += 1
                _discovery.update_progress(current_task, progress, total)
        else:
            ip_addr = ip_obj
            if ip_addr in done_set:
                continue
            _discovery.discover_one_ip(ip_addr)
            done_set.add(ip_addr)
            progress += 1
            _discovery.update_progress(current_task, progress, total)

    return {'progress': total, 'total': total}


@app.task()
def build_explorers(explorers=None, incremental_changes=None):
    explorer = object_type.ExplorerModule()
    explorer.run()


# @app.task()
# def build_topology(topology_types, incremental_changes=None):
#     if not incremental_changes:
#         incremental_changes = {}
#     for topo_type in topology_types:

#     ip_list = ip_list.split(';')
#     to_do_list = []
#     done_set = set()
#     total = 0
#     progress = 0
#     for ip_item in ip_list:
#         if '-' in ip_item:
#             ip_range = IPRange(*ip_item.split('-'))
#             to_do_list.append(ip_range)
#             total += len(ip_range)
#         elif '/' in ip_item:
#             ip_network = IPNetwork(ip_item)
#             to_do_list.append(ip_network)
#             total += len(ip_network)
#         else:
#             ip_address = IPAddress(ip_item)
#             to_do_list.append(ip_address)
#             total += 1
#     for ip_obj in to_do_list:
#         if isinstance(ip_obj, (IPRange, IPNetwork)):
#             for ip_addr in ip_obj:
#                 if ip_addr in done_set:
#                     continue
#                 _discovery.discover_one_ip(ip_addr)
#                 done_set.add(ip_addr)
#                 progress += 1
#                 _discovery.update_progress(current_task, progress, total)
#         else:
#             ip_addr = ip_obj
#             if ip_addr in done_set:
#                 continue
#             _discovery.discover_one_ip(ip_addr)
#             done_set.add(ip_addr)
#             progress += 1
#             _discovery.update_progress(current_task, progress, total)

#     return {'progress': total, 'total': total}
