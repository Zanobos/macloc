import { HTTP } from '@/api'

export default {
  getWalls (cb, ecb) {
    HTTP.get('walls')
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  getWall (id, cb, ecb) {
    HTTP.get('walls/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
