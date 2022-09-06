<script setup>
import { useQuizCreationStore } from "../stores/quizCreation";
import Quiz from "../services/Quiz";
import { useMutation } from "vue-query";

const store = useQuizCreationStore();

const {
  mutate: createQuiz,
  isLoading,
  isError,
  data,
  error,
  isSuccess,
} = useMutation(() => Quiz.createQuiz(store.$state), {
  onSuccess: (data) => {
    console.log(data);
  },
  onError: (error) => {
    alert(error);
  },
});
</script>

<template>
  <div class="mt-12">
    <p class="flex justify-left text-5xl text-white pt-10 pl-20 font-light">
      Gameverse Quiz Creation
    </p>
    <div className="flex flex-wrap lg:flex-nowrap justify-center m-8 p-8">
      <div class="grid grid-cols-1 gap-8 justify-items-center w-8/12">
        <div class="w-full">
          <p class="text-5xl mb-5">Summary</p>
          <br />
          <p class="text-4xl mb-5">Quiz Category: {{ store.category }}</p>
          <br />
          <p class="text-4xl mb-5">Quiz Title: {{ store.title }}</p>
          <br />
          <p class="text-4xl mb-5">
            <span
              class="bg-blue-800 text-white text-3xl font-medium px-5 py-0.5 rounded mr-5"
              >Questions: {{ store.questions.length }}</span
            >
            <router-link
              :to="{
                path: '/QuizCreation',
              }"
              class="text-white bg-green-500 hover:bg-green-600 font-medium rounded-lg text-3xl px-5 py-0.5 mr-2"
            >
              Edit
            </router-link>
          </p>
        </div>
        <div class="w-full mt-10">
          <div
            class="grid grid-cols-1 gap-8 justify-items-center px-10 my-20"
            v-for="(question, index) in store.questions"
          >
            <span
              class="bg-blue-500 w-full text-white text-2xl font-medium mr-2 px-5 py-3 rounded"
              >Q{{ index + 1 }} {{ question.question }}</span
            >
            <div
              class="grid grid-cols-4 gap-8 justify-items-center px-10 w-full"
            >
              <div v-for="(value, key, index) in question.options">
                <span
                  :class="
                    question.answer.includes(key)
                      ? 'bg-green-400'
                      : 'bg-blue-800'
                  "
                  class="text-xl w-full font-medium mr-2 px-5 py-2.5 rounded text-white"
                  >{{ value }}</span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="">
    <hr class="border-4 border-white w-full" />
    <div class="grid grid-cols-1 gap-8 justify-items-center mt-10 w-11/12">
      <div>
        <button
          type="button"
          class="text-white bg-orange-400 hover:bg-orange-500 font-medium rounded-lg text-2xl px-5 py-2.5 mr-5"
        >
          Exit
        </button>

        <button
          class="text-white bg-green-500 hover:bg-green-600 font-medium rounded-lg text-2xl px-5 py-2.5"
          @click="createQuiz"
        >
          Create Quiz
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
