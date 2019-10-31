import request from '@/utils/request'

export function getMapThumbs() {
  return request({
    url: '/maps',
    method: 'get',
  })
}

export function getMap(mapId) {
  return request({
    url: '/maps',
    method: 'get',
    params: {
      name: mapId
    }
  })
}

export function saveMap(data) {
  return request({
    url: '/maps',
    method: 'post',
    data,
  })
}
