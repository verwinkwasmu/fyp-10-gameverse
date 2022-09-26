<script setup>
import {ref} from 'vue'
import {useRoute} from 'vue-router'

const route = useRoute()

const users = ref({})

const response = {
  command: 'Scoreboard',
}

window.websocket.send(JSON.stringify(response))

window.websocket.onmessage = (event) => {
  users.value = JSON.parse(event.data).current_users
  console.log(JSON.parse(event.data))
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
          <p class="float-right mt-10">Question 1 of 3</p>
        </div>
      </div>

      <!--Scoreboard-->
      <div
        class="mx-auto my-auto mt-4 2xl:mt-20 p-4 max-w-xl rounded overflow-hidden font-bold bg-purple-100 text-purple-800"
      >
        <div class="flex text-lg mb-2">
          <div class="w-4/6">Player</div>
          <div class="w-2/6">Score</div>
        </div>

        <div class="flex items-center py-4" v-for="(value, key) in users">
          <div class="w-4/6 flex">
            <p class="pt-2 pl-2">User {{ key }}</p>
          </div>
          <p class="w-2/6 text-lg sm:text-xl">{{ value.score }}</p>
        </div>
      </div>

      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Exit Game
        </button>
        <router-link
          :to="{
            path: `/SoloQuiz/${route.params.lobby_id}/${route.params.client_id}`,
          }"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          move to quiz
        </router-link>
      </footer>
    </div>
  </div>
</template>
