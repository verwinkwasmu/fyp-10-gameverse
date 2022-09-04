import { createRouter, createWebHistory } from "vue-router"
import Chat from "../components/Chat.vue"
import Room from "../pages/Room.vue"
import QuizResult from '../components/QuizResult.vue'
import Podium from '../components/Podium.vue'
import PodiumLoading from '../components/PodiumLoading.vue'
import ScoreBoard from '../components/ScoreBoard.vue'
import TeamQuiz from '../components/TeamQuiz.vue'
import TeamQuizResults from '../components/TeamQuizResults.vue'
import Quizbank from '../components/AllQuizQuestionBank.vue'
import QuizQuestionBank from '../components/AddQuestionFromBank.vue'
import AddedQuizQuestionBank from '../components/AddedQuestionFromBank.vue'



const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/room/:room_id",
            component: Chat
        },
        {
            path: "/testRoom",
            component: Room
        },
        {
            path: "/QuizResult",
            component: QuizResult
        },
        {
            path: "/Podium",
            component: Podium
        },
        {
            path: "/PodiumLoading",
            component: PodiumLoading
        },
        {
            path: "/Scoreboard",
            component: ScoreBoard
        },
        {
            path: "/TeamQuiz",
            component: TeamQuiz
        },
        {
            path: "/TeamQuizResults",
            component: TeamQuiz
        },
        {
            path: "/AllQuizQuestionBank",
            component: Quizbank
        },
        {
            path: "/AddQuestionFromBank",
            component: QuizQuestionBank
        },
        {
            path: "/AddedQuestionFromBank",
            component: AddedQuizQuestionBank
        },
    ]
})

export default router