<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

// use with vue query
import Chat from "../services/Chat";

const route = useRoute();
const client_id = Date.now();
const text = ref("");
const messages = ref([]);
const connection = new WebSocket(`ws://localhost:8080/ws/${route.params.room_id}/${client_id}`);

connection.onopen = () => {
  console.log("connection established");
};
connection.onmessage = (event) => {
  messages.value.push(event.data);
};

const joinRoomId = () => {
  connection.send(text.value);
};
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">

      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">Join Game</div>
      </div>
      
      <div class="flex items-center mt-24 grid grid-flow-row auto-rows-max justify-items-center">
        <div class="text-2xl text-center">Enter Room ID:</div>
        <div class="my-3">
          <input
          v-model="text"
          type="text"
          id="room_id"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-96"
          placeholder="Room ID"
          required
        />
        </div>
        <div class="my-3">
          <button
            type="button"
            class="bg-lime-400 hover:bg-lime-600 text-black hover:text-white font-bold py-4 px-8 mx-2 rounded"
            @click="joinRoomId"
          >
            Join Game
          </button>
      </div>
        </div>
      
    </div>
  </div>
</template>