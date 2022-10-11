import { defineStore } from "pinia";

export const useQuizCreationStore = defineStore("quizCreation", {
  state: () => {
    return {
      title: "",
      category: "",
      questions: [
        {
          question: "",
          options: {
            option_1: "",
            option_2: "",
          },
          answer: [],
          timer: "",
        },
      ],
    };
  },

  actions: {
    addOption(object) {
      let i = Object.keys(object).length;
      object[`option_${i + 1}`] = "";
      console.log(this.questions);
    },
    removeOption(object) {
      let i = Object.keys(object).length;
      delete object[`option_${i}`];
    },
    addQuestion(object) {
      let newQuestion = {
        question: "",
        options: {
          option_1: "",
        },
        answer: "",
        timer: "",
      };
      object.push(newQuestion);
    },
    removeQuestion(object) {
      object.pop();
    },
  },
});
