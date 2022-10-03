<script setup>
import {ref, onMounted} from 'vue'

const users = ref({})

onMounted(() => {
  window.websocket.send(JSON.stringify({command: 'To Podium'}))
})

window.websocket.onmessage = (event) => {
  users.value = JSON.parse(event.data).current_users
  console.log(JSON.parse(event.data))
}
</script>

<template>
  <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <div class="text-4xl font-semibold col-span-2">GameVerse</div>
        <div class="text-2xl col-span-2">Quiz Category</div>
      </div>

      <!--Podium help idk how to move the names w the podium if screen is stretched-->

      <div id="first">First</div>
      <div id="second">Second</div>
      <div id="third">Third</div>

      <div class="flex justify-center items-center mt-32">
        <img src="../assets/podium.png" style="width: 500px" />
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

<style scoped>
#first {
  position: absolute;
  margin-left: 640px;
  margin-top: 80px;
}
#second {
  position: absolute;
  margin-left: 460px;
  margin-top: 140px;
}
#third {
  position: absolute;
  margin-left: 800px;
  margin-top: 170px;
}
</style>
