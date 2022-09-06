<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

// use with vue query
import Chat from "../services/Chat";

const route = useRoute();
const client_id = Date.now();
const text = ref("");
const messages = ref([]);
const connection = new WebSocket(
  `ws://localhost:8080/ws/${route.params.room_id}/${client_id}`
);

connection.onopen = () => {
  console.log("connection established");
};
connection.onmessage = (event) => {
  messages.value.push(event.data);
};

const sendMessage = () => {
  connection.send(text.value);
};
</script>

<template lang="">
  <div>
    <h1 class="text-3xl font-bold underline">Mini Chat App</h1>
    <div>
      <label
        for="first_name"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
      ></label>
      <input
        v-model="text"
        type="text"
        id="first_name"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Send a message!"
        required
      />
    </div>
    <button
      type="button"
      class="text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
      @click="sendMessage"
    >
      Send!
    </button>
    <ul
      class="space-y-1 max-w-md list-disc list-inside text-gray-500 dark:text-gray-400"
    >
      <li v-for="message in messages" :key="message">
        {{ message }}
      </li>
    </ul>
  </div>
</template>
