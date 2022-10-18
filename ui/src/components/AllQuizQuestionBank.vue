<script setup>
import {onMounted, ref} from 'vue'
import Quiz from '../services/Quiz'
import {useQuery} from 'vue-query'

const category = ref('')

const {isLoading, isError, isFetching, data, error, refetch} = useQuery(
  ['questionsByCategory', category],
  () => Quiz.getCategories(category.value),
  {
    retry: 2,
    staleTime: 50000,
    cacheTime: 50000,
  },
)
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font col-span-2">GameVerse Quiz Creation</div>
      </div>
      <div class="mx-auto mt-16 max-w-xl rounded overflow-hidden">
        <div class="flex items-center py-4">
          <div class="w-4/6 flex">
            <p class="text-3xl font col-span-2">Question Bank</p>
          </div>
        </div>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="quizname"
          type="text"
          placeholder="Search Quiz Category"
          v-model="category"
        />
        <div class="basis-1/4">
          <div class="rounded-md shadow">
            <button
              class="flex w-full items-center justify-center rounded-md border border-transparent bg-cyan-600 px-8 py-3 text-base font-medium text-white hover:bg-cyan-700 md:py-1 md:px-7"
              @click="searchCategory"
            >
              Search
            </button>
          </div>
        </div>
        <div>
          <div class="text-sm row-span-2 flow-root">
            <p class="float-left mt-10">Quiz Category (By Latest)</p>
          </div>
        </div>
        <div
          class="flex flex-row pt-5"
          v-for="(category, index) in data"
          :key="index"
        >
          <div class="basis-1/2 pr-4">
            <div class="rounded-md shadow">
              <a
                href="#"
                class="flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 md:py-1 md:px-10"
                >{{ category }}</a
              >
            </div>
          </div>

          <div class="basis-1/4">
            <div class="rounded-md shadow">
              <router-link
                class="flex w-full items-center justify-center rounded-md border border-transparent bg-cyan-600 px-8 py-3 text-base font-medium text-white hover:bg-cyan-700 md:py-1 md:px-7"
                :to="`/addquestionfrombank/${category}`"
                >Open</router-link
              >
            </div>
          </div>
        </div>
      </div>
      <div class="flex justify-center pt-10">
        <router-link
          class="bg-red-400 hover:bg-red-300 text-black font-bold py-2 px-4 rounded hover:text-white"
          :to="{path: '/CreateQuiz'}"
          >Back to Quiz Creation</router-link
        >
      </div>
    </div>
  </div>
</template>
