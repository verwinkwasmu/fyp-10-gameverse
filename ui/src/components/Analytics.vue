<script setup>
import {ref, onBeforeMount, onMounted} from 'vue'
import {useQueryClient} from 'vue-query'
import {useRouter, useRoute} from 'vue-router'
import {useUserIdStore} from '../stores/userId'

const router = useRouter()
const userStore = useUserIdStore()
const queryClient = useQueryClient()

onMounted(() => {
  if (userStore.user == null) {
    router.push({path: `/Login`})
  }

  if (userStore.user.data.id > 0) {
    console.log(userStore.user.id)
    router.push({path: `/`})
  }
})

const signOut = () => {
  let logout = userStore.logout()
  if (logout) {
    // clear current user's vue-query client
    queryClient.clear()
    router.push('/Login')
  }
}
</script>

<template>
  <div style="height: 100%">
    <iframe
      src="https://verwinkwasmu-fyp-10-gameverse-analyticsmain-8vol3m.streamlit.app/?embedded=true"
    ></iframe>
    <footer class="fixed left-0 bottom-6 flex ml-6">
      <router-link to="/">
        <button class="btn-return" @click="signOut">Sign Out</button>
      </router-link>
    </footer>
  </div>
</template>

<style>
html,
body {
  height: 100%;
}
body {
  overflow: hidden;
  margin: 0;
}
iframe {
  height: 100%;
  width: 100%;
  frameborder: 0;
}
#app {
  height: 100%;
}
</style>
