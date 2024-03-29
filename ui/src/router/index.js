import {createRouter, createWebHistory} from 'vue-router'
import QuizResult from '../components/QuizResult.vue'
import Podium from '../components/Podium.vue'
import Analytics from '../components/Analytics.vue'
import TeamQuizLobby from '../components/TeamQuizLobby.vue'
import TeamQuizResults from '../components/TeamQuizResults.vue'
import TeamQuiz from '../components/TeamQuiz.vue'
import Quizbank from '../components/AllQuizQuestionBank.vue'
import QuizQuestionBank from '../components/AddQuestionFromBank.vue'
import TeamQuizHomepageHost from '../components/TeamQuizHomepageHost.vue'
import Home from '../components/Home.vue'
import JoinGame from '../components/JoinGame.vue'
import CreateQuiz from '../components/CreateQuiz.vue'
import MyQuizzes from '../components/MyQuizzes.vue'
import SoloQuiz from '../components/SoloQuiz.vue'
import QuizLobby from '../components/QuizLobby.vue'
import NotScoreboard from '../components/NotScoreboard.vue'
import TeamNotScoreboard from '../components/TeamNotScoreboard.vue'
import AllQuizes from '../components/AllQuizzes.vue'
import Leaderboard from '../components/Leaderboard.vue'
import ViewQuiz from '../components/ViewQuiz.vue'
import Login from '../components/Login.vue'
import UpdateQuiz from '../components/UpdateQuiz.vue'
import UpdateQuizSummary from '../components/UpdateQuizSummary.vue'
import QuizCreation from '../components/QuizCreation.vue'
import QuizCreationSummary from '../components/QuizCreationSummary.vue'
import AddQuestionFromBankForUpdate from '../components/AddQuestionFromBankForUpdate.vue'
import AllQuizQuestionBankForUpdate from '../components/AllQuizQuestionBankForUpdate.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/QuizResult',
      component: QuizResult,
    },
    {
      path: '/Podium',
      component: Podium,
    },
    {
      path: '/Analytics',
      component: Analytics,
    },
    {
      path: '/Scoreboard',
      component: NotScoreboard,
    },
    {
      path: '/TeamQuizLobby/:lobby_id',
      component: TeamQuizLobby,
    },
    {
      path: '/TeamQuizResults',
      component: TeamQuizResults,
    },
    {
      path: '/AllQuizQuestionBank',
      component: Quizbank,
    },
    {
      path: '/AddQuestionFromBank/:category',
      component: QuizQuestionBank,
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
      path: '/SoloQuiz',
      component: SoloQuiz,
    },
    {
      path: '/TeamQuiz',
      component: TeamQuiz,
    },
    {
      path: '/TeamScoreboard',
      component: TeamNotScoreboard,
    },
    {
      path: '/QuizLobby/:lobby_id',
      component: QuizLobby,
      props: (route) => ({query: route.query}),
    },
    {
      path: '/AllQuizzes',
      component: AllQuizes,
    },
    {
      path: '/Leaderboard',
      component: Leaderboard,
    },
    {
      path: '/ViewQuiz/:quiz_id',
      component: ViewQuiz,
    },
    {
      path: '/Login',
      component: Login,
    },
    {
      path: '/UpdateQuiz',
      component: UpdateQuiz,
    },
    {
      path: '/UpdateQuizSummary',
      component: UpdateQuizSummary,
    },
    {
      path: '/AllQuizQuestionBankForUpdate',
      component: AllQuizQuestionBankForUpdate,
    },
    {
      path: '/AddQuestionFromBankForUpdate/:category',
      component: AddQuestionFromBankForUpdate,
    },
  ],
})

export default router
