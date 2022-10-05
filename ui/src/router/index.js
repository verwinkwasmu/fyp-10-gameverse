import {createRouter, createWebHistory} from 'vue-router'
import Room from '../pages/Room.vue'
import QuizResult from '../components/QuizResult.vue'
import Podium from '../components/Podium.vue'
import PodiumLoading from '../components/PodiumLoading.vue'
import TeamQuiz from '../components/TeamQuiz.vue'
import TeamQuizResults from '../components/TeamQuizResults.vue'
import Quizbank from '../components/AllQuizQuestionBank.vue'
import QuizQuestionBank from '../components/AddQuestionFromBank.vue'
import AddedQuizQuestionBank from '../components/AddedQuestionFromBank.vue'
import TeamQuizHomepageHost from '../components/TeamQuizHomepageHost.vue'
import Home from '../components/Home.vue'
import JoinGame from '../components/JoinGame.vue'
import CreateQuiz from '../components/CreateQuiz.vue'
import MyQuizzes from '../components/MyQuizzes.vue'
import RoomLobby from '../components/RoomLobby.vue'
import SoloQuiz from '../components/SoloQuiz.vue'
import QuizLobby from '../components/QuizLobby.vue'
import NotScoreboard from '../components/NotScoreboard.vue'
import AllQuizes from '../components/AllQuizzes.vue'


import {QuizCreation, Chat, QuizCreationSummary} from '../components'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/room/:room_id',
      component: Chat,
    },
    {
      path: '/testRoom',
      component: Room,
    },
    {
      path: '/QuizResult',
      component: QuizResult,
    },
    {
      path: '/Podium',
      component: Podium,
    },
    {
      path: '/PodiumLoading',
      component: PodiumLoading,
    },
    {
      path: '/Scoreboard',
      component: NotScoreboard,
    },
    {
      path: '/TeamQuiz',
      component: TeamQuiz,
    },
    {
      path: '/TeamQuizResults',
      component: TeamQuiz,
    },
    {
      path: '/AllQuizQuestionBank',
      component: Quizbank,
    },
    {
      path: '/AddQuestionFromBank',
      component: QuizQuestionBank,
    },
    {
      path: '/AddedQuestionFromBank',
      component: AddedQuizQuestionBank,
    },
    {
      path: '/TeamQuizHomepageHost',
      component: TeamQuizHomepageHost,
    },
    {
      path: '/QuizCreation',
      component: QuizCreation,
      props: (route) => ({query: route.query}),
    },
    {
      path: '/QuizCreationSummary',
      component: QuizCreationSummary,
    },
    {
      path: '/',
      component: Home,
    },
    {
      path: '/JoinGame',
      component: JoinGame,
    },
    {
      path: '/CreateQuiz',
      component: CreateQuiz,
    },
    {
      path: '/MyQuizzes',
      component: MyQuizzes,
    },
    {
      path: '/RoomLobby/:room_id',
      component: RoomLobby,
    },
    {
      path: '/SoloQuiz',
      component: SoloQuiz,
    },
    {
      path: '/QuizLobby/:lobby_id',
      component: QuizLobby,
    },
    {
      path: '/AllQuizzes',
      component: AllQuizes,
    },
  ],
})

export default router
