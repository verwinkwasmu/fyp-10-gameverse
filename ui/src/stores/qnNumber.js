import {defineStore} from 'pinia'

export const useQnNumberStore = defineStore('qnNumber', {
  state: () => {
    return {
      qnNum: 0,
      score: 0,
      quiz_id: 0,
      user_id: 0,
    }
  },

  actions: {},
})
