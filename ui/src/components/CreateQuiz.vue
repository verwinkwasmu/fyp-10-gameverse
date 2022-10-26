<script setup>
import {ref, onMounted} from 'vue'
import { useRouter, useRoute } from "vue-router";
import {useUserIdStore} from '../stores/userId'

// use with vue query

const client_id = Date.now();
const text = ref("");
const messages = ref([]);

const router = useRouter()
const userStore = useUserIdStore()

onMounted(()=>{

  if (userStore.user == null){
    router.push({path: `/Login`})
  }
})

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
        <div class="text-2xl col-span-2">Create Quiz</div>
      </div>

      <div class="align-middle">
        <div class="text-2xl text-center font-bold mt-8">How do you want to start your quiz?</div>
        <div class="flex justify-center items-center mt-8 grid grid-flow-col auto-cols-max pt-20">
          <div>
            <router-link class="bg-lime-400 hover:bg-lime-600 text-black py-24 px-8 mx-2 rounded w-64 h-80 font-bold hover:text-white" :to="{path: '/AllQuizzes'}">Choose From Quiz Bank</router-link>
          </div>
          <div>
            <router-link class="bg-lime-400 hover:bg-lime-600 text-black py-24 px-8 mx-2 rounded w-64 h-80 font-bold hover:text-white" :to="{path: '/QuizCreation'}">Create Your Own Quiz</router-link>
          </div>
          <div>
          </div>
        </div>
      </div>
      
    </div>
    <footer class="fixed left-10 bottom-5 flex ml-6">
        <router-link to="/">
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          >
            Return
          </button>
        </router-link>
      </footer>
  </div>
</template>