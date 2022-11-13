import axios from 'axios'

const API = () => {
  return axios.create({
    baseURL: 'https://yhb9zv.deta.dev/api',
  })
}

export default {
  async getPlayers() {
    try {
      const response = await API().get('/players')
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  getPlayer(player_id) {
    return API().get(`/player/${player_id}`)
  },
  async addQuizResults(payload) {
    try {
      const response = await API().put('/addQuizResults', payload)
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
}
