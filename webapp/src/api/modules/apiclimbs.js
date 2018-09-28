import { HTTP } from '@/api'

export default {
  getClimbs (cb, ecb) {
    HTTP.get('climbs')
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  getClimb (id, cb, ecb) {
    HTTP.get('climbs/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  postClimbs (climb, cb, ecb) {
    HTTP.post('climbs', climb)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  putClimb (climb, cb, ecb) {
    HTTP.put('climbs/' + climb.id, climb)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  patchClimb (climb, cb, ecb) {
    HTTP.patch('climbs/' + climb.id, climb)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  deleteClimb (id, cb, ecb) {
    HTTP.delete('climbs/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
