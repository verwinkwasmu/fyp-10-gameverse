<script setup>
import {useDark, useToggle} from '@vueuse/core'
import {VueQueryDevTools} from 'vue-query/devtools'
const isDark = useDark()
const toggleDark = useToggle(isDark)
</script>

<template>
  <div>
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
