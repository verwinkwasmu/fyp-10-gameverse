import {defineStore} from 'pinia'
import {toRef} from 'vue'
import {useQuestionBankStore} from './questionBank'

export const useQuizUpdateStore = defineStore('quizUpdate', {
  state: () => ({
    id: '',
    title: '',
    category: '',
    questions: [],
  }),
  actions: {
    addOption(object) {
      let i = Object.keys(object).length
      object[`option_${i + 1}`] = ''
    },
    removeOption(object) {
      let i = Object.keys(object).length
      delete object[`option_${i}`]
    },
    addQuestion() {
      let newQuestion = {
        question: '',
        options: {
          option_1: '',
        },
        answer: '',
        timer: '',
      }
      this.questions.push(newQuestion)
    },
    removeQuestion(object, index) {
      const questionBankStore = useQuestionBankStore()

      if (questionBankStore.addedQuestions.includes(object[index].question)) {
        questionBankStore.removeQuestion(object[index].question)
      }
      object.splice(index, 1)
    },
    update(payload) {
      Object.assign(this, payload)
    },
    addQuestions(questions) {
      for (const question of questions) {
        let newQuestion = {
          question: question.question,
          options: {
            option_1: question.options.option_1,
            option_2: question.options.option_2,
            option_3: question.options.option_3,
            option_4: question.options.option_4,
          },
          answer: question.answer,
          timer: question.timer,
        }
        this.questions.push(newQuestion)
      }
    },
  },
})
