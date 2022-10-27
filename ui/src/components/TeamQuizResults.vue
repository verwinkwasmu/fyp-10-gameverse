<script setup>
import {ref, onMounted} from 'vue'

const scores = ref({})

onMounted(() => {
  window.websocket.send(JSON.stringify({command: 'To Podium'}))
})

window.websocket.onmessage = (event) => {
  scores.value = JSON.parse(event.data).teamScores
}
</script>

<template lang="">
  <div
    class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto"
  >
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">Team Quiz Results</div>
      </div>
    </div>
  <div class="flex items-center justify-center space-x-20 m-0 pb-0 pr-30 pl-30 pt-20">
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
    <p v-else class="text-center text-2xl text-white font-bold">It's a Tie!</p>
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
      <router-link
        to="/"
        class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
      >
        Exit Game
      </router-link>
    </footer>
  </div>
  </div>
</template>
