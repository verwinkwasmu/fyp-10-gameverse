<script setup>
import { ref } from "vue";

defineProps({
  msg: String,
});

const count = ref(0);
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Quiz Category</div>
      </div>

      <!--Loading screen-->
      <div
        class="h-64 w-screen bg-blue-600/50 -ml-16 mt-20 text-center flex justify-center items-center"
      >
        <div class="text-5xl">Podium Results</div>
      </div>

      <!--Exit game button-->
      <footer class="fixed left-10 bottom-10 flex ml-6">
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Exit Game
        </button>
      </footer>
    </div>
  </div>
</template>

<style></style>
