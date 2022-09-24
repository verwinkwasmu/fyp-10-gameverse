<script setup>
import { ref } from "vue";

const participants = ref([
      {id: 0, name: 'Paul'},
      {id: 1, name: 'Richard'},
      {id: 2, name: 'William'},
      {id: 2, name: 'John'},
    ])

defineProps({
  msg: String,
});

const count = ref(0);
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Quiz Lobby</div>
        <div class="text-sm row-span-2 flow-root">
          <p class="float-right mt-10">Waiting for host to start the quiz</p>
        </div>
      </div>
      <!--Scoreboard--> 
      <div
        class="mx-auto p-4 mt-16 max-w-xl rounded overflow-hidden font-bold bg-purple-100 text-purple-800"
      >
        <div class="flex text-lg mb-2">
          <div class="w-4/6">Players in Quiz</div>
        </div>

        <div class="flex items-center py-4" v-for="participant in participants" :key="participant._id">
          
          <div class="w-4/6 flex">
            
            <img
              class="w-6 sm:w-10 mr-2 self-center"
              src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Cowboy_emoji_grande.png?v=1571606089"
            />
            <p>{{ participant.name }}</p>
          </div>
        </div>
      </div>

      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Exit Game
        </button>
      </footer>
    </div>
  </div>
</template>

<style></style>
