import request from '@/utils/request'

export function getExplorers() {
  return request({
    url: '/explorers',
    method: 'get',
  })
}

export function getExplorer(explorerName) {
  return request({
    url: '/explorers',
    method: 'get',
    params: {
      name: explorerName
    }
  })
}
