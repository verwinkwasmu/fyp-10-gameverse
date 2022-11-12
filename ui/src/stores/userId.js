import {defineStore} from 'pinia'
import Player from '../services/Player'
import {useQuizCreationStore} from './quizCreation'
import {useQuizUpdateStore} from './quizUpdate'

export const useUserIdStore = defineStore('userId', {
  state: () => {
    return {
      user: JSON.parse(localStorage.getItem('user')),
    }
  },

  actions: {
    async login(userId) {
      const quizCreationStore = useQuizCreationStore()
      const quizUpdateStore = useQuizUpdateStore()
      try {
        const response = await Player.getPlayer(userId)
        this.user = response
        console.log(response)
        localStorage.setItem('user', JSON.stringify(response))
        quizCreationStore.createdQuiz.user_id = userId
        quizUpdateStore.quiz.user_id = userId
        return response.status
      } catch (err) {
        this.user = null
        localStorage.removeItem('user')
        return err
      }
    },
    logout() {
      const quizCreationStore = useQuizCreationStore()

      this.user = null
      localStorage.removeItem('user')

      // clear store
      localStorage.removeItem('createdQuiz')
      quizCreationStore.$reset()

      return true
    },
  },
})
