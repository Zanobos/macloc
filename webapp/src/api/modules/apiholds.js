import { HTTP } from '@/api'

export default {
  getHolds (cb, ecb) {
    HTTP.get('holds')
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  getHold (id, cb, ecb) {
    HTTP.get('holds/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  postHolds (hold, cb, ecb) {
    HTTP.post('holds', hold)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  putHold (hold, cb, ecb) {
    HTTP.put('holds/' + hold.id, hold)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  patchHold (hold, cb, ecb) {
    HTTP.patch('holds/' + hold.id, hold)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  deleteHold (id, cb, ecb) {
    HTTP.delete('holds/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
