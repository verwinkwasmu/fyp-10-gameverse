<script setup>
import {ref, onBeforeMount, onMounted} from 'vue'
import {useRouter, useRoute} from 'vue-router'
import Player from '../services/Player'
import {useQuery} from 'vue-query'

// GET Players Function
const {
  isLoading,
  isError,
  isFetching,
  isSuccess,
  data: players,
  error: queryError,
} = useQuery(['getPlayers'], () => Player.getPlayers(), {
  retry: 2,
  staleTime: 50000,
  cacheTime: 50000,
})
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-3xl col-span-2">Leaderboard</div>
      </div>
      <div
        v-if="isError"
        class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800"
        role="alert"
      >
        <span class="font-medium">Error Occurred:</span> {{ queryError }}
      </div>
      <div class="align-middle" v-else-if="isSuccess">
        <div class="text-2xl text-center font-bold mt-8">
          Overall Leaderboard
        </div>
        <div
          class="flex justify-center items-center mt-8 grid grid-flow-col auto-cols-max"
        >
          <div>
            <div class="overflow-x-auto relative">
              <table
                class="w-full text-sm text-left text-gray-500 dark:text-gray-400"
              >
                <thead
                  class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
                >
                  <tr>
                    <th scope="col" class="py-3 px-6">Position</th>
                    <th scope="col" class="py-3 px-6">Employee name</th>
                    <th scope="col" class="py-3 px-6">Score</th>
                  </tr>
                </thead>
                <tbody v-for="(player, index) in players" :key="index">
                  <tr
                    class="bg-gray-100 border-b dark:bg-gray-800 dark:border-gray-700"
                  >
                    <th
                      scope="row"
                      class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                    >
                      {{ index + 1 }}
                    </th>
                    <td class="py-4 px-6">
                      {{ player.name }}
                    </td>
                    <td class="py-4 px-6">
                      {{ player.total_points }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="fixed left-10 bottom-5 flex ml-6">
        <router-link to="/">
          <button
            class="btn-return"

          >
            Return
          </button>
        </router-link>
      </footer>
  </div>
</template>
