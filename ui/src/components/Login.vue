<script setup>
import {ref, onMounted} from 'vue'

const users = ref({})

</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto">
    <!--Header-->
    <div class="px-10 pt-10 ml-6 mr-6 ">
      <router-link to="/">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
      </router-link>
    </div>
    
    <div class="flex flex-col items-center justify-center px-6 mx-auto md:h-screen lg:py-0">

      <div class="w-full bg-slate-100 rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
          <div class="px-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                  Log in to your account
              </h1>
              <form class="space-y-4 md:space-y-6" action="#">
                  <div>
                      <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
                      <input type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" required="">
                  </div>

                  <button type="submit" class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Sign in</button>

              </form>
          </div>
      </div>
  </div>

      
  </div>
</template>