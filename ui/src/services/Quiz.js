import axios from 'axios'
import {useQuizObjectStore} from '../stores/quizObject'

const API = () => {
  return axios.create({
    // baseURL: 'https://n08yph.deta.dev/api',
    baseURL: 'http://localhost:8080/api',
  })
}

export default {
  async getQuizzes() {
    try {
      const response = await API().get('/quizzes')
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  async getUserQuizzes(user_id) {
    try {
      const response = await API().get(`/quizzes/user/${user_id}`)
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  async getQuiz(quiz_id) {
    try {
      const response = await API().get(`/quiz/${quiz_id}`)

      // Store the quiz object in the store to prevent render error in soloQuiz and teamQuiz
      const store = useQuizObjectStore()
      store.quiz = response.data

      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  async createQuiz(payload) {
    try {
      const response = await API().post('/create', payload)
      return response.data
    } catch (err) {
      throw err.response.data
    }
  },
  async updateQuiz(payload) {
    try {
      const response = await API().put('/update', payload)
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  async deleteQuiz(quiz_id) {
    try {
      const response = await API().delete(`/delete/${quiz_id}`)
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  async getCategories(category) {
    try {
      const response = await API().get(`/category/?category=${category}`)
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
  async getQuestionsByCategory(category) {
    try {
      const response = await API().get(`/questions/${category}`)
      return response.data
    } catch (err) {
      throw new Error(err)
    }
  },
}
