<template lang="">

    <!-- <p class="flex justify-left text-5xl text-white pt-10 pl-20 font-light">
      Gameverse Quiz
    </p> -->
    <div class="grid grid-rows-2 grid-flow-col gap-2 justify-start">
            <div class="text-5xl font-semibold col-span-2">GameVerse</div>
            <div class="text-2xl col-span-2">Quiz Category</div>
            <div class="text-sm row-span-2 flow-root">
              <p class="float-right mt-10 text-2xl text-white font-bold">You have been invited to play the Movies Quiz!</p>
            </div>
      </div>
    <div class="flex items-center justify-center pt-10 mb-0">
    <!-- <p class="text-2xl text-white font-bold pb-5">
      You have been invited to play the Movies Quiz!
    </p> -->
    
    </div>
    <div class="flex items-center justify-center pt-0 pb-0 mb-0">
    <p class="text-2xl text-white font-bold">
      Select Team
    </p>
    </div>
    <div class="flex items-center justify-center space-x-20 mt-10 mb-20 pr-20 pl-20">
  
    <button class="w-full h-40 text-indigo-100 transition-colors duration-150 bg-blue-700 rounded-lg focus:shadow-outline hover:bg-blue-400">
      <div class="font-bold">
      Join Blue Team
      </div>
      <div class="items-left">
        <ul id="example-1">
          <li v-for="item in items" :key="item.message">
            {{ item.message }}
          </li>
        </ul>
      </div>
    </button>
    <button class="w-full h-40 text-indigo-100 transition-colors duration-150 bg-red-700 rounded-lg focus:shadow-outline hover:bg-pink-400">
      <div class="font-bold">
      Join Red Team
      </div>
      <div class="items-left">
        <ol>
          <li>1. Peter Tan</li>
          <li>2. Jane Liu</li>
          <li></li>
        </ol>
      </div>
    </button>
    </div>
    <div class="flex items-center justify-between space-x-40 m-20 pt-0">
  
    <button class="items-centre pl-20 pr-20 h-20 text-indigo-100 border border-black bg-pink-300 rounded-none focus:shadow-outline">
      Exit Game
    </button>
    <button class="items-centre pl-20 pr-20 h-20 text-black bg-green-300 rounded-none focus:shadow-outline">
      30s till start!
    </button>
    </div>

</template>

<style>
  body {
    background-image: url('../assets/background.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
  }
</style>

// <script>
// import { TeamQuiz } from '@vue/composition-api'

// export default defineComponent({
//   setup() {
    
//   },
// })
// var example1 = new Vue({
//   el: '#example-1',
//   data: {
//     items: [
//       { message: 'Foo' },
//       { message: 'Bar' }
//     ]
//   }
// })
// </script>
