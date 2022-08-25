import { createRouter, createWebHistory } from "vue-router"
import Chat from "../components/Chat.vue"
import TeamQuiz from "../components/TeamQuiz.vue"
import TeamQuizResults from "../components/TeamQuizResults.vue"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/room/:room_id",
            component: Chat
        },
        {
            path: "/TeamQuiz",
            component: TeamQuiz
        },
        {
            path: "/TeamQuizResults",
            component: TeamQuizResults
        }
    ]
})

export default router