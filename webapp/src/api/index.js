import axios from 'axios'

export const HTTP = axios.create({
  baseURL: `http://localhost:5000/api/`
})

export function encodeQueryData (data) {
  let ret = []
  for (let d in data) {
    ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(data[d]))
  }
  return '?' + ret.join('&')
}
