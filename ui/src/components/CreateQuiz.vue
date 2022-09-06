<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

// use with vue query

const route = useRoute();
const client_id = Date.now();
const text = ref("");
const messages = ref([]);


const joinRoomId = () => {
  connection.send(text.value);
};
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">

      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Create Quiz</div>
      </div>
      
      <div class="flex justify-center items-center mt-8 grid grid-flow-col auto-cols-max">
        <div>
          <button
            type="button"
            class="bg-green-400 hover:bg-green-700 text-white font-bold py-24 px-8 mx-2 rounded w-64 h-80"
            @click="createNewQuiz">
            Create A GameVerse Quiz
          </button>
        </div>
        <div>
          <button
            type="button"
            class="bg-green-400 hover:bg-green-700 text-white font-bold py-24 px-8 mx-2 rounded w-64 h-80"
            @click="createNewQuiz">
            Customise Your Own Quiz
          </button>
        </div>
        <div>
          <button
            type="button"
            class="bg-green-400 hover:bg-green-700 text-white font-bold py-24 px-8 mx-2 rounded w-64 h-80"
            @click="createNewQuiz">
            Quiz Bank
          </button>
        </div>
      </div>
      
    </div>
  </div>
</template>