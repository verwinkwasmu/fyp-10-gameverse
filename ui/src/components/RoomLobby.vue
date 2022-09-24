<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

// use with vue query
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

const joinRoomId = () => {
  connection.send(text.value);
};
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-3 gap-2">
        <div class="text-5xl font-semibold col-span-2">GameVerse Quiz</div>
        <div class="text-2xl col-span-2">Room ID</div>
      </div>
    </div>

    <div class="grid grid-flow-col grid-cols-3 px-10 py-6 mx-6 flex items-center">
      <div
        class="
          col-span-2
          flex
          items-center
          grid grid-flow-row
          auto-rows-max
          justify-items-center
          justify-center
          gap-4
        "
      >
        <div class="text-2xl">
          The GameVerse quiz will begin soon.
        </div>
        <div class="text-2xl">Waiting for all players...</div>
      </div>

      <!-- table of participants -->
      <div class="bg-neutral-200 rounded p-4 max-w-xs place-self-center">
        <div class="overflow-x-auto relative">
          <table
            class="w-full text-sm text-left text-gray-500 dark:text-gray-400"
          >
            <thead class="text-xs text-gray-900 uppercase dark:text-gray-400 border-b border-gray-700">
              <tr>
                <th scope="col" class="py-3 px-6">Participant</th>
                <th scope="col" class="py-3 px-6">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th
                  scope="row"
                  class="
                    py-4
                    px-6
                    font-medium
                    text-gray-900
                    whitespace-nowrap
                    dark:text-white
                  "
                >
                  John Doe
                </th>
                <td class="py-4 px-6">
                  <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Remove</a>
              </td>
              </tr>
              <tr>
                <th
                  scope="row"
                  class="
                    py-4
                    px-6
                    font-medium
                    text-gray-900
                    whitespace-nowrap
                    dark:text-white
                  "
                >
                  Verwin Kwa
                </th>
                <td class="py-4 px-6">
                  <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Remove</a>
              </td>
              </tr>
              <tr>
                <th
                  scope="row"
                  class="
                    py-4
                    px-6
                    font-medium
                    text-gray-900
                    whitespace-nowrap
                    dark:text-white
                  "
                >
                  Rafael B.
                </th>
                <td class="py-4 px-6">
                  <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Remove</a>
              </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="fixed bottom-0 w-full">
      <router-link to="/JoinGame" tag="button">
        <button
          type="button"
          class="
            bg-red-500
            hover:bg-red-700
            text-white
            font-bold
            py-4
            px-8
            mx-4
            my-8
            rounded
            tracking-wide
          ">
          Exit Game
        </button>
      </router-link>
    </div>
  </div>
</template>