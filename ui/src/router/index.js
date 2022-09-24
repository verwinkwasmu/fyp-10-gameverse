import { createRouter, createWebHistory } from "vue-router"
import Room from "../pages/Room.vue"
import QuizResult from '../components/QuizResult.vue'
import Podium from '../components/Podium.vue'
import PodiumLoading from '../components/PodiumLoading.vue'
import ScoreBoard from '../components/ScoreBoard.vue'
import TeamQuiz from '../components/TeamQuiz.vue'
import TeamQuizResults from '../components/TeamQuizResults.vue'
import Home from '../components/Home.vue'
import JoinGame from '../components/JoinGame.vue'
import CreateQuiz from '../components/CreateQuiz.vue'
import MyQuizzes from '../components/MyQuizzes.vue'
import RoomLobby from '../components/RoomLobby.vue'
import SoloQuiz from '../components/SoloQuiz.vue'


import { QuizCreation, Chat, QuizCreationSummary } from "../components";

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
            path: "/QuizCreation",
            component: QuizCreation,
            props: (route) => ({ query: route.query }),
        },
        {
            path: "/QuizCreationSummary",
            component: QuizCreationSummary,
        },
        {
            path: "/",
            component: Home
        },
        {
            path: "/JoinGame",
            component: JoinGame
        },
        {
            path: "/CreateQuiz",
            component: CreateQuiz
        },
        {
            path: "/MyQuizzes",
            component: MyQuizzes
        },
        {
            path: "/RoomLobby/:room_id",
            component: RoomLobby
        },
        {
            path: "/SoloQuiz/:room_id",
            component: SoloQuiz
        },
    ]
});

export default router;
