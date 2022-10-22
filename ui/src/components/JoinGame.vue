<script setup>
import {ref, onMounted} from 'vue'
import {useUserIdStore} from '../stores/userId'
import {useRouter} from 'vue-router'

const router = useRouter()
const text = ref('')
let isOpen = ref(false)

const userStore = useUserIdStore()

onMounted(() => {

  if (userStore.user == null){
    router.push({path: `/Login`})
  }
})

const joinSoloRoomId = () => {
  if (text.value != ''){
    router.push({path: `/QuizLobby/${text.value}`})
  }
}

const joinTeamRoomId = () => {
  if (text.value != ''){
    router.push({path: `/TeamQuizLobby/${text.value}`})
  }
}

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

      <div
        class="flex items-center mt-24 grid grid-flow-row auto-rows-max justify-items-center"
      >
        <div class="text-2xl text-center">Enter Lobby ID:</div>
        <div class="my-3">
          <input
            v-model="text"
            type="text"
            id="room_id"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-96"
            placeholder="Lobby ID"
            required
          />
        </div>
        <div class="my-3">
          <button
            type="button"
            class="bg-lime-400 hover:bg-lime-600 text-black hover:text-white font-bold py-4 px-8 mx-2 rounded"
            @click="isOpen = true"
            
          >
            Join Game
          </button>
        </div>


        <div
          v-show="isOpen"
          class="
            absolute
            inset-0
            flex
            items-center
            justify-center
            bg-gray-700 
            bg-opacity-70
          "
        >
          <div class="max-w-2xl p-6 mx-4 bg-slate-200 rounded-md shadow-xl">
            <div class="flex items-center justify-between">
              <h3 class="text-2xl text-black">Choose Game</h3>
              <svg
                @click="isOpen = false"
                xmlns="http://www.w3.org/2000/svg"
                class="w-8 h-8 text-red-900 cursor-pointer hover:text-red-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </div>
            <div class="flex grid grid-flow-col mt-4 gap-4 h-16">
              <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 rounded font-bold text-xl"  @click="joinSoloRoomId">
                Solo
              </button>
              <button class="bg-lime-500 hover:bg-lime-700 text-black hover:text-white py-2 px-8 rounded font-bold text-xl"  @click="joinTeamRoomId">
                Team
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>
