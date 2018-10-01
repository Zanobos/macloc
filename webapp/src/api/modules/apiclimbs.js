import { HTTP, encodeQueryData } from '@/api'

export default {
  getClimbs (cb, ecb, page, perPage, userId) {
    let data = {}
    data.page = page
    data.per_page = perPage
    data.user_id = userId
    let queryString = encodeQueryData(data)
    HTTP.get('climbs' + queryString)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  getClimb (cb, ecb, id) {
    HTTP.get('climbs/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  postClimbs (cb, ecb, climb) {
    HTTP.post('climbs', climb)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  putClimb (cb, ecb, climb) {
    HTTP.put('climbs/' + climb.id, climb)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  patchClimb (cb, ecb, climb) {
    HTTP.patch('climbs/' + climb.id, climb)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  deleteClimb (cb, ecb, id) {
    HTTP.delete('climbs/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
