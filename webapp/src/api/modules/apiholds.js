import { HTTP, encodeQueryData } from '@/api'

export default {
  getHolds (cb, ecb, page, perPage, wallId) {
    let data = {}
    data.page = page
    data.per_page = perPage
    data.wall_id = wallId
    let queryString = encodeQueryData(data)
    HTTP.get('holds' + queryString)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  getHold (cb, ecb, id) {
    HTTP.get('holds/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  postHolds (cb, ecb, hold) {
    HTTP.post('holds', hold)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  putHold (cb, ecb, hold) {
    HTTP.put('holds/' + hold.id, hold)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  patchHold (cb, ecb, hold) {
    HTTP.patch('holds/' + hold.id, hold)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  deleteHold (cb, ecb, id) {
    HTTP.delete('holds/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
