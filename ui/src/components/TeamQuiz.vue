<template lang="">
    <p class="text-5xl text-white pt-10 pl-20 font-light">
      Gameverse Quiz
    </p>
    <div class="flex items-center justify-center pt-40 mb-0">
    <p class="text-2xl text-white font-bold">
      You have been invited to play the Movies Quiz!
    </p>
    <br/>
    <br/>
    <br/>
    <p class="text-2xl text-white font-bold">
      Select Team
    </p>
    </div>
    <div class="flex items-center justify-center space-x-20 m-20 pr-20 pl-20">
  
    <button class="w-full h-40 text-indigo-100 transition-colors duration-150 bg-blue-700 rounded-lg focus:shadow-outline hover:bg-blue-400">
      Join Blue Team
    </button>
    <button class="w-full h-40 text-indigo-100 transition-colors duration-150 bg-red-700 rounded-lg focus:shadow-outline hover:bg-pink-400">
      Join Red Team
    </button>
    </div>
    <div class="flex items-center justify-between space-x-40 m-20 pt-20">
  
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
    background-image: url('background.jpeg');
  }
</style>