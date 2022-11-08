<script setup>
import {useQuizUpdateStore} from '../stores/quizUpdate'
import Quiz from '../services/Quiz'
import {useMutation, useQueryClient} from 'vue-query'
import {useRouter} from 'vue-router'
import {useQuestionBankStore} from '../stores/questionBank'

const queryClient = useQueryClient()
const store = useQuizUpdateStore()
const questionBankStore = useQuestionBankStore()
const router = useRouter()

const {
  mutate: updateQuiz,
  isLoading,
  isError,
  data,
  error,
  isSuccess,
} = useMutation(() => Quiz.updateQuiz(store.quiz), {
  onSuccess: (data) => {
    // Reset stores
    store.$reset()
    questionBankStore.$reset()

    // Refetch getQuizzes Query
    queryClient.invalidateQueries('getUserQuizzes')

    // Redirect to MyQuizzes page
    router.push({path: `/MyQuizzes`})
  },
  onError: (error) => {
    alert(error)
  },
})
</script>

<template>
  <div
    class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto"
  >
    <!--Header-->
    <div class="grid grid-rows-2 grid-flow-col gap-2 px-10 pt-10 ml-6 mr-6">
      <router-link to="/">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
      </router-link>
      <div class="text-2xl col-span-2">Summary of Quiz</div>
    </div>

    <div
      class="flex grid grid-flow-row auto-rows-max items-center mt-4 mx-4 gap-4 items-center justify-center"
    >
      <div class="grid grid-flow-row gap-4 mb-4">
        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div
            class="w-60 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            Quiz Title
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
          >
            {{ store.quiz.title }}
          </div>
        </div>

        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div
            class="w-60 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            Number of Questions
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
          >
            {{ store.quiz.questions.length }}
          </div>
        </div>

        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div
            class="w-60 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            Category
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
          >
            {{ store.quiz.category }}
          </div>
        </div>
      </div>
      <div class="text-2xl font-bold -mb-4">Questions</div>

      <div
        class="flex grid grid-flow-row auto-rows-max gap-4"
        v-for="(question, index) in store.quiz.questions"
        :key="index"
      >
        <div class="grid grid-flow-col auto-cols-max gap-4 w-full">
          <div
            class="w-96 justify-items-stretch bg-indigo-700 px-8 py-3 mt-6 text-base font-medium text-white"
          >
            {{ question.question }}
          </div>
          <div
            class="grid justify-items-end bg-blue-900 px-8 py-3 mt-6 text-base font-medium text-white"
          >
            Time: {{ question.timer }}
          </div>
        </div>

        <div v-for="(option, index) in question.options" :key="index">
          <div
            v-if="index == question.answer"
            class="grid grid-flow-col auto-cols-max gap-4"
          >
            <div
              class="font-bold text-white rounded-full bg-green-500 flex items-center justify-center w-12 h-12 align-middle"
            >
              ✓
            </div>
            <div
              class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-green-500"
            >
              {{ option }}
            </div>
          </div>

          <div v-else class="grid grid-flow-col auto-cols-max gap-4">
            <div
              class="font-bold text-white rounded-full bg-red-500 flex items-center justify-center w-12 h-12 align-middle"
            >
              ✖
            </div>
            <div
              class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-blue-900"
            >
              {{ option }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <div className="" class="mt-14 mb-4">
      <div class="grid grid-cols-1 gap-8 justify-items-center mt-10">
        <div>
          <router-link to="/UpdateQuiz">
            <button
              type="button"
              class="btn-return"
            >
              Back
            </button>
          </router-link>

          <button
            class="btn-complete"
            @click="updateQuiz"
          >
            Update Quiz
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
body {
  background-image: url('../assets/bg.png');
}
</style>
