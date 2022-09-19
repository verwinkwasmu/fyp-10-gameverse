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
        <div class="text-2xl col-span-2">My Quizzes</div>
      </div>
      

      <div class="flex grid grid-flow-row auto-rows-max items-center mt-7 mx-7 gap-4 justify-center">
        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div class="font-bold text-gray-700 rounded-full bg-white flex items-center justify-center w-12 h-12 align-middle	">1</div>
          <div class="w-80 p-4 items-center justify-center bg-indigo-700 rounded">Trivia 101</div>
          <div class="w-30 p-4 bg-blue-900 text-white items-center rounded justify-center text-center">9 Questions</div>
          <button class="bg-purple-500 hover:bg-purple-700 text-white py-2 px-8 mx-2 rounded font-bold">Edit Game</button>
          <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 mx-2 rounded font-bold">Start Game</button>
          <button class="bg-red-700 hover:bg-red-900 text-white py-2 px-8 mx-2 rounded font-bold">Delete</button>
        </div>
        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div class="font-bold text-gray-700 rounded-full bg-white flex items-center justify-center w-12 h-12 align-middle	">2</div>
          <div class="w-80 p-4 items-center justify-center bg-indigo-700 rounded">Geography</div>
          <div class="w-30 p-4 bg-blue-900 text-white items-center rounded justify-center text-center">9 Questions</div>
          <button class="bg-purple-500 hover:bg-purple-700 text-white py-2 px-8 mx-2 rounded font-bold">Edit Game</button>
          <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white hover:text-white py-2 px-8 mx-2 rounded font-bold">Start Game</button>
          <button class="bg-red-700 hover:bg-red-900 text-white py-2 px-8 mx-2 rounded font-bold">Delete</button>
        </div>
        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div class="font-bold text-gray-700 rounded-full bg-white flex items-center justify-center w-12 h-12 align-middle	">3</div>
          <div class="w-80 p-4 items-center justify-center bg-indigo-700 rounded">Greatest Rock Hits</div>
          <div class="w-30 p-4 bg-blue-900 text-white items-center rounded justify-center text-center">9 Questions</div>
          <button class="bg-purple-500 hover:bg-purple-700 text-white py-2 px-8 mx-2 rounded font-bold">Edit Game</button>
          <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 mx-2 rounded font-bold">Start Game</button>
          <button class="bg-red-700 hover:bg-red-900 text-white py-2 px-8 mx-2 rounded font-bold">Delete</button>
        </div>
      </div>
      
    </div>
  </div>
</template>