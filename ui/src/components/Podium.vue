<script setup>
import {ref, onMounted} from 'vue'
import {useMutation} from 'vue-query'
import {useRouter} from 'vue-router'
import Player from '../services/Player'
import {useQnNumberStore} from '../stores/qnNumber'
import {useQuizObjectStore} from '../stores/quizObject'

const router = useRouter()
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

const sortPlayers = (users) => {
  let sortUsers = []

  for (let user in users) {
    sortUsers.push([users[user]['name'], users[user]['score']])
  }

  sortUsers.sort(function (a, b) {
    return b[1] - a[1]
  })
  return sortUsers.slice(0, 3)
}

const backToHome = () => {
  window.websocket.close()
  router.push({path: '/'})
}
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-4xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Quiz Category</div>
      </div>

      <div
        class="grid grid-flow-row flex justify-center items-center mt-20 gap-2"
      >
        <div
          v-for="user in sortPlayers(users)"
          :key="user"
          class="columns-[10rem]"
        >
          <p class="flex justify-center items-center font-semibold text-2xl">
            {{ user[0] }}
          </p>
          <p class="flex justify-center items-center">{{ user[1] }} Points</p>
        </div>
        <div class="col-span-3">
          <img src="../assets/podium_new.png" style="width: 500px" />
        </div>
      </div>

      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">
        <button class="btn-exitQuiz" @click="backToHome">Exit Game</button>
      </footer>
    </div>
  </div>
</template>
