<script setup>
import {ref, onBeforeMount, onMounted} from 'vue'
import {useQueryClient} from 'vue-query'
import {useRouter, useRoute} from 'vue-router'
import {useUserIdStore} from '../stores/userId'

const router = useRouter()
const userStore = useUserIdStore()
const queryClient = useQueryClient()
onMounted(() => {
  if (userStore.user == null) {
    router.push({path: `/Login`})
  }
})

const signOut = () => {
  let logout = userStore.logout()
  if (logout) {
    // clear current user's vue-query client
    queryClient.clear()
    router.push('/Login')
  }
}
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
          <div class="flex justify-start">
            <div class="text-5xl font-semibold col-span-2">GameVerse</div>
          </div>
          <div class="text-2xl flex justify-start">Home</div>

       <div class="flex justify-end pt-4">
        <router-link to="/MyQuizzes" tag="button" class="pr-2">
          <button
            class="bg-teal-400 hover:bg-teal-600 text-black font-bold py-2 px-4 rounded w-40 hover:text-white"
          >
            My Quizzes
          </button>
        </router-link>
        <router-link to="/Leaderboard" tag="button">
          <button
            class="bg-teal-400 hover:bg-teal-600 text-black font-bold py-2 px-4 rounded w-40 hover:text-white"
          >
            Leaderboard
          </button>
        </router-link>
        </div>
      </div>

      <div class="flex justify-center items-center mt-7 pt-8">
        <router-link to="/JoinGame" tag="button">
          <button
            class="bg-yellow-200 hover:bg-yellow-400 text-black hover:text-white font-bold py-8 px-12 mx-2 rounded w-64 h-80"
          >
          <img src="../assets/planet_red.png">
          <div class="pt-10">
            Join Game
          </div>
          </button>
        </router-link>
        <router-link to="/CreateQuiz" tag="button">
          <button
            class="bg-fuchsia-400 hover:bg-fuchsia-600 text-black hover:text-white font-bold py-8 px-12 mx-2 rounded w-64 h-80"
          >
          <img src="../assets/planet_blue.png">
          <div class="pt-10">
            Create Quiz
          </div>
          </button>
        </router-link>
      </div>

      <footer class="fixed left-10 bottom-5 flex ml-6">
        <router-link to="/">
          <button
            class="btn-return"
            @click="signOut"
          >
            Sign Out
          </button>
        </router-link>
      </footer>
    </div>
  </div>
</template>
