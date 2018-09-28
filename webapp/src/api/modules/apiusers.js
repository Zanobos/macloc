import { HTTP } from '@/api'

export default {
  getUsers (cb, ecb) {
    HTTP.get('users')
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  getUser (id, cb, ecb) {
    HTTP.get('users/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  postUsers (user, cb, ecb) {
    HTTP.post('users', user)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  putUser (user, cb, ecb) {
    HTTP.put('users/' + user.id, user)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  patchUser (user, cb, ecb) {
    HTTP.patch('users/' + user.id, user)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  },
  deleteUser (id, cb, ecb) {
    HTTP.delete('users/' + id)
      .then(
        (response) => cb(response),
        (error) => ecb(error)
      )
  }
}
