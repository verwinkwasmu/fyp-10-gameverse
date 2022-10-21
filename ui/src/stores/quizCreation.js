import {defineStore} from 'pinia'
import {useQuestionBankStore} from './questionBank'

export const useQuizCreationStore = defineStore('quizCreation', {
  state: () => {
    return {
      title: '',
      category: '',
      questions: [
        {
          question: '',
          options: {
            option_1: '',
            option_2: '',
          },
          answer: '',
          timer: '',
        },
      ],
    }
  },

  actions: {
    addOption(object) {
      let i = Object.keys(object).length
      object[`option_${i + 1}`] = ''
    },
    removeOption(object) {
      let i = Object.keys(object).length
      delete object[`option_${i}`]
    },
    addQuestion(object) {
      let newQuestion = {
        question: '',
        options: {
          option_1: '',
        },
        answer: '',
        timer: '',
      }
      object.push(newQuestion)
    },
    removeQuestion(object, index) {
      const questionBankStore = useQuestionBankStore()

      if (questionBankStore.addedQuestions.includes(object[index].question)) {
        questionBankStore.removeQuestion(object[index].question)
      }
      object.splice(index, 1)
    },
  },
})
