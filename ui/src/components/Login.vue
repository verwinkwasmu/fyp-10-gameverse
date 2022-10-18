<script setup>
import { ref, onBeforeMount, onMounted} from "vue";
import { useRouter, useRoute } from "vue-router";
import Player from '../services/Player'
import {useUserIdStore} from '../stores/userId'


const router = useRouter()
const userId = ref()
var isError = ref(false)
const userStore = useUserIdStore()
let loading = ref(false)

onMounted(()=>{
  if (userStore.user != null){
    router.push({path: `/`})
  }
})

async function onSubmit() {
    loading.value = true
    isError.value = false
    let login = await userStore.login(userId.value)
    if (login == 200){
      router.push({path: `/`})
    }
    else{
      loading.value = false
      isError.value = true
    }
}



</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto">
    <!--Header-->
    <div class="px-10 pt-10 ml-6 mr-6 ">
      <div class="text-5xl font-semibold col-span-2">GameVerse</div>
    </div>

    
    <div class="flex flex-col items-center justify-center px-6 mx-auto sm:py-28">
      
      <div class="w-full bg-slate-200 rounded-md shadow dark:border md:mt-0 sm:max-w-md xl:p-0">
        <div class="px-6 space-y-4 md:space-y-6 sm:p-8">
            <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
              Log in to your account
            </h1>
            <div>
              <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">User ID</label>
              <input v-model="userId" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-96" placeholder="Please enter your User ID" required="" @keyup.enter="onSubmit">
            </div>
          
            <div v-if="isError==true" class="flex p-4 bg-red-100 rounded-lg dark:bg-red-200" role="alert">
              <svg aria-hidden="true" class="flex-shrink-0 w-5 h-5 text-red-700 dark:text-red-800" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>
              <span class="sr-only">Info</span>
              <div class="ml-3 text-sm font-medium text-red-700 dark:text-red-800">
                Please enter a valid User ID
              </div>
            </div>

            <button v-if="loading == false" @click="onSubmit" class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" >Sign in</button>
            <button v-else class="w-full text-white bg-blue-600 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" disabled>
              <svg aria-hidden="true" class="inline mr-1 w-4 h-4 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                  <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
              </svg>
              Loading ...
            </button>


          </div>
      </div>
  </div>

      
  </div>
</template>
