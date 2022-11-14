<script setup>
import {ref, onMounted} from 'vue'
import {useUserIdStore} from '../stores/userId'
import {useRouter, useRoute} from 'vue-router'
import {useQueryClient, useQuery, useMutation} from 'vue-query'
import Quiz from '../services/Quiz'
import {useQuizUpdateStore} from '../stores/quizUpdate'
import colors from 'tailwindcss/colors'

const store = useQuizUpdateStore()
const queryClient = useQueryClient()
const router = useRouter()
let isOpen = ref(false)
const userStore = useUserIdStore()

onMounted(() => {
  if (userStore.user == null) {
    router.push({path: `/Login`})
  }
})

const deleteSuccess = ref(true)
const showAlert = ref(false)
let modalQuizId = ref()

// GET Quizzes Function
const {
  isLoading,
  isError,
  isFetching,
  isSuccess,
  data: quizzes,
  error: queryError,
} = useQuery(
  ['getUserQuizzes'],
  () => Quiz.getUserQuizzes(userStore.user.data.id),
  {
    retry: 2,
    staleTime: 50000,
    cacheTime: 50000,
  },
)


// DELETE Quiz Function
const {mutate: deleteQuiz, error: deleteError} = useMutation(
  (quizId) => Quiz.deleteQuiz(quizId),
  {
    onSuccess: () => {
      // Refetch getQuizzes Query
      queryClient.invalidateQueries('getUserQuizzes')
      deleteSuccess.value = true
      showAlert.value = true
      setTimeout(() => {
        showAlert.value = false
      }, 5000)
    },
    onError: (error) => {
      deleteSuccess.value = true
      showAlert.value = true
      setTimeout(() => {
        showAlert.value = false
      }, 5000)
    },
  },
)

const startSoloGame = (quizId) => {
  let lobby_id = Math.floor(100000 + Math.random() * 900000)
  router.push({
    path: `/QuizLobby/${lobby_id}`,
    query: {quiz_id: quizId, isHost: true},
  })
}

const startTeamGame = (quizId) => {
  let lobby_id = Math.floor(100000 + Math.random() * 900000)
  router.push({
    path: `/TeamQuizLobby/${lobby_id}`,
    query: {quiz_id: quizId, isHost: true},
  })
}

const moveToUpdateQuiz = (quiz) => {
  store.$patch({
    quiz: {
      id: quiz.id,
      user_id: quiz.user_id,
      title: quiz.title,
      category: quiz.category,
      questions: [],
    },
  })
  store.addQuestions(quiz.questions)
  router.push({
    path: `/UpdateQuiz`,
  })
}

const modalOpen = (quizId) => {
  modalQuizId.value = quizId
  isOpen.value = true
}
</script>

<template>
  <div
    class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto"
  >
    <div class="p-10 ml-6 mr-6">
      <!--Header-->
      <div class="grid grid-rows-2 grid-flow-col gap-2">
        <router-link to="/">
          <div class="text-5xl font-semibold col-span-2">GameVerse</div>
        </router-link>
        <div class="text-2xl col-span-2">My Quizzes</div>
      </div>
      <div
        v-if="isError"
        class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800"
        role="alert"
      >
        <span class="font-medium">Error Occurred:</span> {{ queryError }}
      </div>
      <div
        v-else-if="quizzes.length > 0"
        class="flex grid grid-flow-row auto-rows-max items-center mt-7 mx-7 gap-4 justify-center"
      >

        <div
          class="grid grid-flow-col auto-cols-max gap-2"
          v-for="(quiz, index) in quizzes"
          :key="index"
        >
          <div
            class="font-bold text-gray-700 rounded-full bg-white flex items-center justify-center w-12 h-12 align-middle"
          >
            {{ index + 1 }}
          </div>
          <div
            class="w-60 p-4 items-center justify-center bg-indigo-700 rounded"
          >
            {{ quiz.title }}
          </div>
          <div
            class="w-40 p-4 items-center justify-center bg-indigo-700 rounded"
          >
            {{ quiz.category }}
          </div>
          <div
            class="p-4 bg-blue-900 text-white items-center w-40 rounded justify-center text-center"
          >
            {{ quiz.questions.length }} Questions
          </div>
          <button
            class="btn-edit"
            @click="moveToUpdateQuiz(quiz)"
          >
            Edit Game
          </button>
          <button
            class="btn-proceed"
            @click="modalOpen(quiz.id)"
          >
            Start Game
          </button>
          <button
            class="btn-delete"
            @click="deleteQuiz(quiz.id)"
          >
            Delete
          </button>
          

          <div
            v-show="isOpen"
            class="absolute inset-0 flex items-center justify-center bg-gray-700 bg-opacity-70"
          >
            <div class="max-w-2xl p-6 mx-4 bg-slate-200 rounded-md shadow-xl">
              <div class="flex items-center justify-between">
                <h3 class="text-2xl text-black">Choose Game</h3>
                <svg
                  @click="isOpen = false"
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-8 h-8 text-red-900 cursor-pointer hover:text-red-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
              <div class="flex grid grid-flow-col mt-4 gap-4 h-16">
                <button
                  class="btn-proceed"
                  @click="startSoloGame(modalQuizId)"
                >
                  Solo
                </button>
                <button
                  class="btn-proceed"
                  @click="startTeamGame(modalQuizId)"
                >
                  Team
                </button>
              </div>
              
            </div>
          </div>
        </div>
      </div>
      <div v-else-if="quizzes.length == 0" class="align-middle">
        <div class="text-2xl text-center font-bold mt-8">
          No Quizzes
        </div>
        <div
          class="flex justify-center items-center mt-8 grid grid-flow-col auto-cols-max"
        >
        <router-link to="/createquiz">
          <button
            class="btn-proceed"
          >
            Proceed to create a quiz
          </button>
        </router-link>
        </div>
      </div>
    </div>
    
    <div
      v-if="deleteSuccess && showAlert"
      id="toast-success"
      class="flex absolute top-5 right-5 items-center p-4 mb-4 w-full max-w-xs text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800"
      role="alert"
    >
      <div
        class="inline-flex flex-shrink-0 justify-center items-center w-8 h-8 text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-green-200"
      >
        <svg
          aria-hidden="true"
          class="w-5 h-5"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
            clip-rule="evenodd"
          ></path>
        </svg>
        <span class="sr-only">Check icon</span>
      </div>
      <div class="ml-3 text-sm font-normal">Quiz deleted successfully.</div>
    </div>
    <div
      v-if="!deleteSuccess && showAlert"
      id="toast-danger"
      class="flex absolute top-5 right-5 items-center p-4 mb-4 w-full max-w-xs text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800"
      role="alert"
    >
      <div
        class="inline-flex flex-shrink-0 justify-center items-center w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200"
      >
        <svg
          aria-hidden="true"
          class="w-5 h-5"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
            clip-rule="evenodd"
          ></path>
        </svg>
        <span class="sr-only">Error icon</span>
      </div>
      <div class="ml-3 text-sm font-normal">
        Error Occurred: {{ deleteError }}
      </div>
      
    </div>
    <footer class="fixed left-10 bottom-5 flex ml-6">
        <router-link to="/">
          <button
            class="btn-return"

          >
            Return
          </button>
        </router-link>
      </footer>
  </div>
</template>
