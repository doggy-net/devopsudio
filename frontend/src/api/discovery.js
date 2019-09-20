import request from '@/utils/request'

export function startDiscovery(data) {
  return request({
    url: '/discovery',
    method: 'post',
    data,
  })
}

export function getDiscoveryStatus(taskId) {
  return request({
    url: '/discovery',
    method: 'get',
    params: { taskId },
  })
}
