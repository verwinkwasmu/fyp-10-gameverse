import {defineStore} from 'pinia'
import Player from '../services/Player'

export const useUserIdStore = defineStore('userId', {
  state: () => {
    return {
      user: JSON.parse(localStorage.getItem('user')),
    }
  },

  actions: {
    async login(userId){
      try{
        const response = await Player.getPlayer(userId)
        this.user = response
        localStorage.setItem('user', JSON.stringify(response))
        return response.status
      } catch (err) {
        this.user = null
        localStorage.removeItem('user')
        return err;
      }
    },
    logout() {
      this.user = null
      localStorage.removeItem('user')
      return true
    }
  },
})
