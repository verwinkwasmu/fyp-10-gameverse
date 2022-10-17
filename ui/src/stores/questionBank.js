import {defineStore} from 'pinia'

export const useQuestionBankStore = defineStore('questionBank', {
  state: () => {
    return {
      addedQuestions: [],
    }
  },

  actions: {
    addQuestion(questionTitle) {
      this.addedQuestions.push(questionTitle)
    },
    removeQuestion(questionTitle) {
      let index = this.addedQuestions.indexOf(questionTitle)
      this.addedQuestions.splice(index, 1)
    },
  },
})
