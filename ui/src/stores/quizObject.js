import { defineStore } from "pinia";

export const useQuizObjectStore = defineStore("quizObject", {
    state: () => {
        return {
            quiz: {},
        };
    },

    actions: {},
});
