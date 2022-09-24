import { defineStore } from "pinia";

export const useQnNumberStore = defineStore("qnNumber", {
    state: () => {
        return {
            qnNum: 0,
            score: 0
        };
    },

    actions: {},
});
