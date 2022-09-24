<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">

      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font col-span-2">GameVerse Quiz</div>
      </div>
      <div
        class="mx-auto max-w-l rounded overflow-hidden">
        <div class="flex items-center py-4">
          <div class="w-4/6 flex">
            <p class="text-xl font col-span-2">Select Quiz Format</p>
          </div>
        </div>
        <div>
            <div class="flex space-x-10">                
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">Solo Contest</router-link>
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">Team Competition</router-link>
            </div>
        </div>
      </div>

        <div class="mx-auto max-w-l rounded overflow-hidden pt-10">
        <div class="flex items-center py-4">
          <div class="w-4/6 flex">
            <p class="text-xl font col-span-2">Select Quiz Category</p>
            <div class="pl-40">
                <router-link class="flex items-center justify-center transition-colors bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">Create Quiz</router-link>
            </div>
          </div>
        </div>
        <div>
            <div class="flex space-x-10">                
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">General Knowlegde</router-link>
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">Movies</router-link>
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">History</router-link>
            </div>
            <div class="flex space-x-10 pt-5">                
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">Technology</router-link>
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">80's Songs</router-link>
                <router-link class="flex items-center justify-center transition-colors w-60 h-20 bg-indigo-900 rounded-lg focus:shadow-outline hover:bg-indigo-400" :to="{path: '/'}">Science</router-link>
            </div>
        </div>
      </div>
      <div class="pt-10 gridh-56 grid grid-cols-3 gap-4 content-end content-end">
        <div class="pr-5">
          <router-link class="bg-gray-400 hover:bg-gray-300 text-white font-bold py-2 px-4 rounded" :to="{path: '/AllQuizQuestionBank'}">Start Quiz</router-link>
        </div>
        <div class="pt-4">
          <router-link class="bg-red-400 hover:bg-red-300 text-white font-bold py-2 px-4 rounded" :to="{path: '/AllQuizQuestionBank'}">Exit Game</router-link>
        </div>
      </div>
    </div>
  </div>
</template>