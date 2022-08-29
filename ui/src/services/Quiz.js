import axios from "axios";

const API = () => {
  return axios.create({
    baseURL: "https://n08yph.deta.dev/api",
  });
};

// just a sample, not the actual one
export default {
  async getQuizzes() {
    try {
      const response = await API().get("/quizzes");
      return response.data;
    } catch (err) {
      return err;
    }
  },
  getQuiz(quiz_id) {
    return API().get(`/quiz/${quiz_id}`);
  },
  createQuiz(payload) {
    return API().post("/create", payload);
  },
  updateQuiz(payload) {
    return API().put("/update", payload);
  },
  deleteQuiz(quiz_id) {
    return API().delete(`/quiz/${quiz_id}`);
  },
};
