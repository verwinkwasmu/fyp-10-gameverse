<script setup>
import {ref, onMounted} from 'vue'
import {useQnNumberStore} from '../stores/qnNumber'
import {useQuizObjectStore} from '../stores/quizObject'
import {useRouter} from 'vue-router'
import Player from '../services/Player'
import {useMutation} from 'vue-query'

const router = useRouter()
const scores = ref({})
const users = ref({})
const qnNumStore = useQnNumberStore()
const quizObjectStore = useQuizObjectStore()

const {
  mutate: addQuizResults,
  isLoading,
  isError,
  data,
  error,
  isSuccess,
} = useMutation((payload) => Player.addQuizResults(payload), {
  onSuccess: (data) => {},
  onError: (error) => {
    alert(error)
  },
})

onMounted(() => {
  if (qnNumStore.user_id.includes('Host')) {
    window.websocket.send(JSON.stringify({command: 'To Podium'}))
  }
})

window.websocket.onmessage = (event) => {
  if (JSON.parse(event.data).command == 'To Podium') {
    scores.value = JSON.parse(event.data).teamScores
    users.value = JSON.parse(event.data).current_users
    // to make sure that only users (not host) gets to have their scores recorded
    if (qnNumStore.user_id.toString() in users.value) {
      const payload = {
        id: parseInt(qnNumStore.user_id),
        score: users.value[qnNumStore.user_id].score,
        category: quizObjectStore.quiz.category,
        start_time: JSON.parse(event.data).start_time,
        end_time: JSON.parse(event.data).end_time,
        quizTitle: quizObjectStore.quiz.title,
      }
      addQuizResults(payload)
    }
  }
}

const backToHome = () => {
  window.websocket.close()
  router.push({path: '/'})
}
</script>

<template lang="">
  <div
    class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto"
  >
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>

        <div class="text-2xl col-span-2">Team Quiz Results</div>
      </div>
    </div>
    <div
      class="flex items-center justify-center space-x-20 m-0 pb-0 pr-30 pl-30 pt-20"
    >
      <!-- <img src="../assets/winner.png" class="w-24" /> -->
    </div>
    <div class="flex items-center justify-center">
      <p
        v-if="scores.red > scores.blue"
        class="text-center text-2xl text-white font-bold"
      >
        Red Team won!
      </p>
      <p
        v-else-if="scores.red < scores.blue"
        class="text-center text-2xl text-white font-bold"
      >
        Blue Team won!
      </p>
      <p v-else class="text-center text-2xl text-white font-bold">
        It's a Tie!
      </p>
    </div>
    <div class="m-10 p-0">
      <p class="text-center text-lg text-white font-bold">Points:</p>
    </div>
    <div class="flex items-center justify-center space-x-0 mr-20 ml-20 pt-0">
      <button
        class="items-centre pl-20 pr-20 h-20 text-indigo-100 bg-red-700 rounded-none focus:shadow-outline text-2xl font-bold"
      >
        {{ scores.red }}
      </button>
      <button
        class="items-centre pl-20 pr-20 h-20 text-indigo-100 bg-blue-700 rounded-none focus:shadow-outline text-2xl font-bold"
      >
        {{ scores.blue }}
      </button>
    </div>
    <div class="flex items-center justify-between space-x-40 m-20 pt-20">
      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">
        <button class="btn-exitQuiz" @click="backToHome">Exit Game</button>
      </footer>
    </div>
  </div>
</template>
