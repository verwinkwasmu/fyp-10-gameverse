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
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">Question Bank</div>
      </div>
      <div class="mx-auto mt-16 max-w-xl rounded overflow-hidden">

        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="quizname"
          type="text"
          placeholder="Search Quiz Category"
          v-model="category"
        />
        <div class="basis-1/4">
          <div class="rounded-md shadow pt-3">
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
          class="grid grid-cols-3 gap-4 pt-5"
          v-for="(category, index) in data"
          :key="index"
        >
          <div class="col-span-2">
            <div class="rounded-md shadow">
              <div
                class="flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white md:py-1 md:px-10" 
                >{{ category }}</div
              >
            </div>
          </div>

          <div class="basis-1/4">
            <div class="rounded-md shadow">
              <router-link
                class="flex w-full items-center justify-center rounded-md border border-transparent bg-cyan-600 px-8 py-3 text-base font-medium text-white hover:bg-cyan-700 md:py-1 md:px-7"
                :to="`/AddQuestionFromBankForUpdate/${category}`"
                >Open</router-link
              >
            </div>
          </div>
        </div>
      </div>
      <div class="flex justify-center pt-10">
        <router-link
          class="btn-return hover:text-white"
          :to="{path: '/UpdateQuiz'}"
          >Back to Quiz Update</router-link
        >
      </div>
    </div>
  </div>
</template>
