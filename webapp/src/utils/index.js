export function getWallImg (id) {
  var images = require.context('@/assets/img/walls/', false, /\.png$/)
  return images('./wall' + id + '.png')
}
