import axios from 'axios'

const API = () => {
  return axios.create({
    baseURL: 'https://n08yph.deta.dev/api',
    // baseURL: 'http://localhost:8080/api',
  })
}

export default {
  async getQuizzes() {
    try {
      const response = await API().get('/quizzes')
      return response.data
    } catch (err) {
      return err
    }
  },
  getQuiz(quiz_id) {
    return API().get(`/quiz/${quiz_id}`)
  },
  async createQuiz(payload) {
    try {
      const response = await API().post('/create', payload)
      return response.data
    } catch (err) {
      return err
    }
  },
  async updateQuiz(payload) {
    try {
      const response = await API().post('/update', payload)
      return response.data
    } catch (err) {
      return err
    }
  },
  async deleteQuiz(quiz_id) {
    try {
      const response = await API().delete(`/delete/${quiz_id}`)
      return response.data
    } catch (err) {
      return err
    }
  },
  async getCategories(category) {
    try {
      const response = await API().get(`/category/?category=${category}`)
      return response.data
    } catch (err) {
      return err
    }
  },
  async getQuestionsByCategory(category) {
    try {
      const response = await API().get(`/questions/${category}`)
      return response.data
    } catch (err) {
      return err
    }
  },
}
