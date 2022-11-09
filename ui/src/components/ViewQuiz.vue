<script setup>
import {ref, onMounted, onBeforeMount} from 'vue'
import {useRouter, useRoute} from 'vue-router'
import {useUserIdStore} from '../stores/userId'
import Quiz from '../services/Quiz'

const quizzes = ref([])
const router = useRouter()
const route = useRoute()
const quiz = ref()
const userStore = useUserIdStore()

onBeforeMount(() => {
  getData()

  if (userStore.user == null) {
    router.push({path: `/Login`})
  }
})

const getData = async () => {
  const response = await Quiz.getQuizzes()
  quizzes.value = response

  for (let i = 0; i < quizzes.value.length; i++) {
    if (quizzes.value[i].id == route.params.quiz_id) {
      quiz.value = quizzes.value[i]
    }
  }
}
</script>

<template>
  <div
    class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto"
  >
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">View Questions</div>
      </div>

      <div
        class="flex grid grid-flow-row auto-rows-max items-center mt-7 mx-7 gap-4 items-center justify-center"
      >
        <div class="grid grid-flow-row gap-4 mb-12">
          <div class="grid grid-flow-col auto-cols-max gap-4">
            <div
              class="w-60 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
            >
              Quiz Title
            </div>
            <div
              class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
            >
              {{ quiz.title }}
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
              {{ quiz.questions.length }}
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
              {{ quiz.category }}
            </div>
          </div>
        </div>

        <div class="text-2xl font-bold">Questions</div>

        <div
          class="flex grid grid-flow-row auto-rows-max gap-4"
          v-for="(question, index) in quiz.questions"
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

        <div class="flex justify-center pt-10">
          <div class="pr-4 pt-2">
            <router-link
              class="btn-return"
              :to="{path: '/AllQuizzes'}"
              >Back to Quizzes</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
