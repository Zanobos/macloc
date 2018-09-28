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
  },
  postWalls (wall, cb, ecb) {
    HTTP.post('walls', wall)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  putWall (wall, cb, ecb) {
    HTTP.put('walls/' + wall.id, wall)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  patchWall (wall, cb, ecb) {
    HTTP.patch('walls/' + wall.id, wall)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  deleteWall (id, cb, ecb) {
    HTTP.delete('walls/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
