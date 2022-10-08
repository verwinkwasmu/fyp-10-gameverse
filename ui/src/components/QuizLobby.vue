<script setup>
import {ref} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {useQnNumberStore} from '../stores/qnNumber'

const route = useRoute()
const router = useRouter()
const client_id = route.query.isHost
  ? 'Host' + Date.now()
  : Date.now().toString()
const quiz_id = ref()
const users = ref({})
const qnNumStore = useQnNumberStore()
qnNumStore.user_id = client_id
const url = `http://localhost:5173/QuizLobby/${route.params.lobby_id}`
const countdowntimer = ref(3)

window.websocket = new WebSocket(
  `ws://localhost:8080/ws/${route.params.lobby_id}/${client_id}/${route.query.quiz_id}`,
)

window.websocket.onopen = () => {
  console.log('connection established')
}

window.websocket.onmessage = (event) => {
  if (!isNaN(event.data)) {
    quiz_id.value = event.data
    console.log(quiz_id.value)
  }

  if (JSON.parse(event.data).command == 'Start Game') {
    console.log('start game')
    moveToQuestion()
  } else {
    users.value = JSON.parse(event.data)
    console.log(users.value.current_users)
  }
}

const clicker = ref(false)
const timer = ref()

function countdownstart() {
  window.websocket.send(JSON.stringify({command: 'Start'}))
}

function moveToQuestion() {
  clicker.value = true

  setTimeout(routenext, 3000)

  let timerCountdown = setInterval(() => {
    countdowntimer.value--
    if (countdowntimer.value == 0) {
      clearInterval(timerCountdown)
    }
  }, 1000)
}
function routenext() {
  let quizId = route.query.quiz_id ? route.query.quiz_id : quiz_id.value
  qnNumStore.quiz_id = quizId
  router.push({path: `/SoloQuiz`})
}
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">
          Quiz Lobby ID: {{ route.params.lobby_id }}
          <br />
          Share Lobby Link: {{ url }}
        </div>
        <div class="text-sm row-span-2 flow-root">
          <p class="float-right mt-10">Waiting for host to start the quiz</p>
        </div>
      </div>
      <!--Scoreboard-->
      <div v-if="!clicker">
        <div
          class="mx-auto p-4 mt-16 max-w-xl rounded overflow-hidden font-bold bg-purple-100 text-purple-800"
        >
          <div class="flex text-lg mb-2">
            <div class="w-4/6">Players in Quiz</div>
          </div>

          <div
            class="flex items-center py-4"
            v-for="(value, user_id) in users.current_users"
            :key="user_id"
          >
            <div class="w-4/6 flex">
              <img
                class="w-6 sm:w-10 mr-2 self-center"
                src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Cowboy_emoji_grande.png?v=1571606089"
              />
              <p>{{ user_id }}</p>
            </div>
          </div>
        </div>
      </div>

      <div v-else-if="clicker">
        <div class="text-7xl mt-12 text-center">
          <div>Are you ready?</div>
          <div class="text-9xl mt-20">{{ countdowntimer }}</div>
        </div>
      </div>

      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">

        <router-link to="/" tag="button">
            <button
              class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
            >
              Exit Game
            </button>
        </router-link>
      </footer>

      <footer class="fixed right-10 bottom-10 flex ml-6">
        <!-- button is just for host to use -->
        <button
          v-if="client_id.toString().includes('Host')"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          @click="countdownstart()"
        >
          Start Game
        </button>
      </footer>
    </div>
  </div>
</template>

<style></style>
