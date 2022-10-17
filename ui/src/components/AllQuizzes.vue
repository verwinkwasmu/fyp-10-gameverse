<script setup>
import {ref, onMounted} from 'vue'
import { useRouter, useRoute } from "vue-router";
import Quiz from '../services/Quiz'

const quizzes = ref([])
const router = useRouter()
let isOpen = ref(false);

onMounted(() => {
  getData()
})

const getData = async () => {
  const response = await Quiz.getQuizzes()
  quizzes.value = response
  console.log(quizzes.value)
}

const startSoloGame = (quizId) => {
  let lobby_id = Math.floor(100000 + Math.random() * 900000)
  router.push({
    path: `/QuizLobby/${lobby_id}`,
    query: {quiz_id: quizId, isHost: true},
  })
}

const startTeamGame = (quizId) => {
  let lobby_id = Math.floor(100000 + Math.random() * 900000)
  router.push({
    path: `/TeamQuizLobby/${lobby_id}`,
    query: {quiz_id: quizId, isHost: true},
  })
}

</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto">
    <div class="p-10 ml-6 mr-6 ">

      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">All Quizzes</div>
      </div>
      

      <div class="flex grid grid-flow-row auto-rows-max items-center mt-7 mx-7 gap-3 justify-center ">

        <div class="grid grid-flow-col auto-cols-max gap-4" v-for="(quiz,index) in quizzes" :key="index">

          <div class="font-bold text-gray-700 rounded-full bg-white flex items-center justify-center w-12 h-12 align-middle	mt-1">
            {{index +1}}
          </div>

          <div class="w-80 p-4 items-center justify-center bg-indigo-700 rounded">
            {{quiz.title}}
          </div>

          <div class="w-30 p-4 bg-blue-900 text-white items-center rounded justify-center text-center">
            Questions: {{quiz.questions.length}}
          </div>

          <router-link :to="`/ViewQuiz/${quiz.id}`" tag="button">
            <button class="bg-purple-500 hover:bg-purple-700 text-white py-2 px-8 rounded font-bold h-full">View Quiz</button>
          </router-link>

          <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 rounded font-bold" @click="isOpen = true">
            Start Game
          </button>

          <div
            v-show="isOpen"
            class="
              absolute
              inset-0
              flex
              items-center
              justify-center
              bg-gray-600 
              bg-opacity-20
            "
          >
            <div class="max-w-2xl p-6 mx-4 bg-slate-200 rounded-md shadow-xl">
              <div class="flex items-center justify-between">
                <h3 class="text-2xl text-black">Choose Game</h3>
                <svg
                  @click="isOpen = false"
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-8 h-8 text-red-900 cursor-pointer hover:text-red-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
              <div class="flex grid grid-flow-col mt-4 gap-4 h-16">
                <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 rounded font-bold text-xl"  @click="startSoloGame(quiz.id)">
                  Solo
                </button>
                <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 rounded font-bold text-xl"  @click="startTeamGame(quiz.id)">
                  Team
                </button>
              </div>
            </div>
          </div>


        </div>
      </div>
      
    </div>
  </div>
</template>