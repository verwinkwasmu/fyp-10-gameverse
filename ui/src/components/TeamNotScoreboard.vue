<script setup>
import {ref, onMounted} from 'vue'
import {useRouter} from 'vue-router'
import {useQnNumberStore} from '../stores/qnNumber'
import {useQuizCreationStore} from '../stores/quizCreation'

const teamScores = ref({})
const router = useRouter()
const qnNumStore = useQnNumberStore()
const quizStore = useQuizCreationStore()

onMounted(() => {
  window.websocket.send(JSON.stringify({command: 'Scoreboard'}))
})

window.websocket.onmessage = (event) => {
  if (JSON.parse(event.data).command == 'Next Question') {
    router.push({path: '/TeamQuiz'})
  } else if (JSON.parse(event.data).command == 'To Podium') {
    router.push({path: '/TeamQuizResults'})
  } else {
    teamScores.value = JSON.parse(event.data).teamScores
    console.log(teamScores.value)
  }
}

const nextQuestion = () => {
  window.websocket.send(JSON.stringify({command: 'Next Question'}))
}

const moveToPodium = () => {
  window.websocket.send(JSON.stringify({command: 'To Podium'}))
}
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-4xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Quiz Category</div>
        <div class="text-sm row-span-2 flow-root">
          <p class="float-right mt-10">
            Question {{ qnNumStore.qnNum }} of
            {{ quizStore.quiz.questions.length }}
          </p>
        </div>
      </div>

      <!--Scoreboard-->
      <div
        class="mx-auto my-auto mt-4 2xl:mt-20 p-4 max-w-xl rounded overflow-hidden font-bold bg-purple-100 text-purple-800"
      >
        <div class="flex text-lg mb-2">
          <div class="w-4/6">Team</div>
          <div class="w-2/6">Score</div>
        </div>
        <div v-if="teamScores.red >= teamScores.blue">
          <div class="flex items-center py-4">
            <div class="w-4/6 flex">
              <img
                class="w-6 sm:w-10 mr-2 self-center"
                src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Cowboy_emoji_grande.png?v=1571606089"
              />
              <p class="pt-2 pl-2">Red</p>
            </div>
            <p class="w-2/6 text-lg sm:text-xl">{{ teamScores.red }}</p>
          </div>
          <div class="flex items-center py-4">
            <div class="w-4/6 flex">
              <img
                class="w-6 sm:w-10 mr-2 self-center"
                src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Cowboy_emoji_grande.png?v=1571606089"
              />
              <p class="pt-2 pl-2">Blue</p>
            </div>
            <p class="w-2/6 text-lg sm:text-xl">{{ teamScores.blue }}</p>
          </div>
        </div>
        <div v-else>
          <div class="flex items-center py-4">
            <div class="w-4/6 flex">
              <img
                class="w-6 sm:w-10 mr-2 self-center"
                src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Cowboy_emoji_grande.png?v=1571606089"
              />
              <p class="pt-2 pl-2">Blue</p>
            </div>
            <p class="w-2/6 text-lg sm:text-xl">{{ teamScores.blue }}</p>
          </div>
          <div class="flex items-center py-4">
            <div class="w-4/6 flex">
              <img
                class="w-6 sm:w-10 mr-2 self-center"
                src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Cowboy_emoji_grande.png?v=1571606089"
              />
              <p class="pt-2 pl-2">Red</p>
            </div>
            <p class="w-2/6 text-lg sm:text-xl">{{ teamScores.red }}</p>
          </div>
        </div>
      </div>

      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mr-5"
        >
          Exit Game
        </button>
        <button
          v-if="
            qnNumStore.qnNum < quizStore.quiz.questions.length &&
            qnNumStore.user_id.includes('Host')
          "
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          @click="nextQuestion"
        >
          Next Question
        </button>
        <button
          v-else-if="qnNumStore.user_id.includes('Host')"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          @click="moveToPodium"
        >
          To Podium
        </button>
      </footer>
    </div>
  </div>
</template>
