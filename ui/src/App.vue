<script setup>
import { useDark, useToggle } from "@vueuse/core";
import { VueQueryDevTools } from "vue-query/devtools";
const isDark = useDark();
const toggleDark = useToggle(isDark);

// need to set this as a dynamic variable
const room_id = 1
</script>

<template>
  <div>
    <!-- <div>
      <p>isDark: {{ isDark }}</p>
      <button
        type="button"
        class="text-white bg-gradient-to-r from-teal-400 via-teal-500 to-teal-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-teal-300 dark:focus:ring-teal-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
        @click="toggleDark()"
      >
        Change Mode
      </button>
    </div> -->
    <!-- <router-link :to="`/room/${room_id}`">Join Chat</router-link>
    <router-link :to="`/testRoom/`">Join Test Room</router-link> -->
    <router-view />
  </div>
</template>

<style scoped>
html.dark {
  color-scheme: dark;
}
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
