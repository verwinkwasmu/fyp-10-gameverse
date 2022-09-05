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
        <div class="text-4xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Quiz Category</div>
        <div class="text-sm row-span-2 flow-root">
          <p class="float-right mt-10">Question 1 of 3</p>
        </div>
      </div>

      <div class="grid grid-flow-row grid-col-1 gap-1 mx-auto my-auto">
        <div class="flex justify-center mt-24 mb-5">
          <img
            src="../assets/correct.png"
            style="width: 170px; height: 175px"
          />
        </div>
        <div class="text-lg 2xl:text-2xl font-bold text-center">That's correct!</div>
        <div class="text-center 2xl:text-lg">+10 points</div>
      </div>
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
</template>

<style scoped></style>
