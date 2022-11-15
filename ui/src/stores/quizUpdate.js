import {defineStore} from 'pinia'
import {useQuestionBankStore} from './questionBank'
import {useStorage} from '@vueuse/core'

export const useQuizUpdateStore = defineStore('quizUpdate', {
  state: () => ({
    quiz: useStorage('quiz', {
      id: '',
      user_id: '',
      title: '',
      category: '',
      questions: [],
    }),
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
      this.quiz.questions.push(newQuestion)
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
          options: {},
          answer: question.answer,
          timer: question.timer,
        }

        for (const [key, val] of Object.entries(question.options)) {
          newQuestion.options[key] = val
        }
        this.quiz.questions.push(newQuestion)
      }
    },
  },
})
