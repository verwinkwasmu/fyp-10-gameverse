import { createRouter, createWebHistory } from "vue-router"
import Chat from "../components/Chat.vue"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/chat",
            component: Chat
        }
    ]
})

export default router