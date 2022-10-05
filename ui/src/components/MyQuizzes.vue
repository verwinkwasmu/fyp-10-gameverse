<script setup>
import {ref, onMounted} from 'vue'
import {useRouter, useRoute} from 'vue-router'
import Quiz from '../services/Quiz'

const quizzes = ref([])
const router = useRouter()
onMounted(() => {
  getData()
})

const getData = async () => {
  const response = await Quiz.getQuizzes()
  quizzes.value = response
  console.log(quizzes.value)
}

const startGame = (quizId) => {
  let lobby_id = Math.floor(100000 + Math.random() * 900000)
  router.push({
    path: `/QuizLobby/${lobby_id}`,
    query: {quiz_id: quizId, isHost: true},
  })
}
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">My Quizzes</div>
      </div>

      <div
        class="flex grid grid-flow-row auto-rows-max items-center mt-7 mx-7 gap-4 justify-center"
      >
        <div
          class="grid grid-flow-col auto-cols-max gap-4"
          v-for="(quiz, index) in quizzes"
          :key="index"
        >
          <div
            class="font-bold text-gray-700 rounded-full bg-white flex items-center justify-center w-12 h-12 align-middle"
          >
            {{ index + 1 }}
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded"
          >
            {{ quiz.title }}
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded"
          >
            {{ quiz.category }}
          </div>
          <div
            class="w-30 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            {{ quiz.questions.length }} Questions
          </div>
          <button
            class="bg-purple-500 hover:bg-purple-700 text-white py-2 px-8 mx-2 rounded font-bold"
          >
            Edit Game
          </button>
          <button
            class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 mx-2 rounded font-bold"
            @click="startGame(quiz.id)"
          >
            Start Game
          </button>
          <button
            class="bg-red-700 hover:bg-red-900 text-white py-2 px-8 mx-2 rounded font-bold"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
