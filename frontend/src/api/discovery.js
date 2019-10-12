import request from '@/utils/request'

export function startDiscovery(data) {
  return request({
    url: '/discovery',
    method: 'post',
    data,
  })
}

export function stopDiscovery() {
  return request({
    url: '/discovery',
    method: 'delete',
  })
}

export function getDiscoveryStatus() {
  return request({
    url: '/discovery',
    method: 'get',
  })
}
