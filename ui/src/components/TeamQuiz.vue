<script setup>
import Quiz from '../services/Quiz'
import {ref, onMounted, onBeforeMount} from 'vue'
import {useQnNumberStore} from '../stores/qnNumber'
import {useRoute, useRouter} from 'vue-router'
import {useQuizObjectStore} from '../stores/quizObject'
import {useQuery} from 'vue-query'

const router = useRouter()
const route = useRoute()

const store = useQuizObjectStore()
const qnNumStore = useQnNumberStore()
const qnCorrect = ref(null)
const qnAnswered = ref(false)
const timer = ref()
const answer_input = ref(null)
const totalQn = ref()
const score = ref(0)

// GET Single Quiz by quiz_id
const {
  isLoading,
  isError,
  isFetching,
  data,
  error: queryError,
  isSuccess,
} = useQuery(
  ['quizById'],
  async () => {
    const quizData = await Quiz.getQuiz(qnNumStore.quiz_id)
    if (qnNumStore.qnNum < quizData.questions.length) {
      setTimer(
        quizData.questions.length,
        quizData.questions[qnNumStore.qnNum].timer,
      )
    }
    return quizData
  },
  {
    retry: 2,
    staleTime: 50000,
    cacheTime: 50000,
  },
)

window.websocket.onmessage = (event) => {
  if (JSON.parse(event.data).command == 'Team has answered') {
    qnAnswered.value = true
    qnCorrect.value = JSON.parse(event.data).correct
    score.value = JSON.parse(event.data).teamScore
  } else if (JSON.parse(event.data).command == 'Show Team Scoreboard') {
    qnNumStore.qnNum += 1
    router.push({path: '/TeamScoreboard'})
  }
}

onMounted(() => {
  if (qnNumStore.qnNum > 0) {
    setTimer(
      data.value.questions.length,
      data.value.questions[qnNumStore.qnNum].timer,
    )
  }
})
function setTimer(questionsLength, questionTimer) {
  totalQn.value = questionsLength
  timer.value = questionTimer

  let timerCountdown = setInterval(() => {
    timer.value--
    if (timer.value == 0) {
      clearInterval(timerCountdown)
      if (!qnAnswered.value) {
        checkAnswers()
      }
    }
  }, 1000)
}

function showAnswer(event) {
  qnAnswered.value = true
  answer_input.value = event
  checkAnswers()
}

function checkAnswers() {
  if (answer_input.value == null) {
    answer_input.value = ''
  }

  let answer_key = data.value.questions[qnNumStore.qnNum].answer
  score.value = 0
  if (
    data.value.questions[qnNumStore.qnNum].options[answer_key] ==
    answer_input.value
  ) {
    qnCorrect.value = true
    qnAnswered.value = true
    score.value += 10 * timer.value
    answer_input.value = null
  } else {
    qnCorrect.value = false
    qnAnswered.value = true
    answer_input.value = null
  }

  const response = {
    command: 'Done',
    score: score.value,
    correct: qnCorrect.value,
  }
  window.websocket.send(JSON.stringify(response))
}

const moveToScoreboard = () => {
  window.websocket.send(JSON.stringify({command: 'Scoreboard'}))
}
</script>

<template>
  <div id="Quiz">
    <div
      v-if="isError"
      class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800"
      role="alert"
    >
      <span class="font-medium">Error Occurred:</span> {{ queryError }}
    </div>
    <div
      v-else-if="isSuccess"
      class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white"
    >
      <div class="p-10 ml-6 mr-6">
        <!--Header-->
        <div class="grid grid-rows-2 grid-flow-col gap-2">
          <div class="text-4xl font-semibold col-span-2">GameVerse</div>
          <div class="text-2xl col-span-2">{{ data.category }}</div>
          <div v-if="!qnAnswered" class="text-sm row-span-2 flow-root">
            <p class="float-right mt-10">
              Question {{ qnNumStore.qnNum + 1 }} of {{ totalQn }}
            </p>
          </div>
        </div>

        <div v-if="!qnAnswered">
          <div
            class="h-24 w-screen bg-blue-600/50 -ml-16 mt-2 mb-8 text-center flex justify-center items-center"
          >
            <div class="text-4xl">
              <div>{{ data.questions[qnNumStore.qnNum].question }}</div>
            </div>
          </div>

          <div class="grid grid-cols-6 gap-4">
            <span v-if="timer != 0" class="font-mono text-5xl countdown">
              {{ timer }}
            </span>

            <div class="col-start-2 col-span-4">
              <div
                class="grid grid-rows-2 grid-cols-2 gap-0 place-content-stretch"
              >
                <button
                  class="button h-24 m-2 box-border rounded-lg hover:bg-blue-900"
                  v-for="(option, index) in data.questions[qnNumStore.qnNum]
                    .options"
                  :key="index"
                  :value="option"
                  v-html="option"
                  @click.stop="showAnswer(option)"
                  :disabled="qnNumStore.user_id.includes('Host')"
                ></button>
              </div>
            </div>
          </div>
          <div class="grid justify-items-center">
          <div v-if="qnNumStore.user_id.includes('Host')" 
            class="grid justify-center pt-2 p-4 mb-4 text-xl text-amber-800 bg-amber-100 rounded-lg dark:bg-amber-200 dark:text-amber-800 w-max" >
                    You do not need to answer the question!
            </div>
          </div>
        </div>

        <div
          v-else-if="
            qnCorrect &&
            qnAnswered &&
            timer == 0 &&
            !qnNumStore.user_id.includes('Host')
          "
        >
          <div class="grid grid-flow-row grid-col-1 gap-1">
            <div class="flex justify-center mt-24 mb-5">
              <img
                src="../assets/correct.png"
                style="width: 170px; height: 175px"
              />
            </div>
            <div class="text-lg font-bold text-center">That's correct!</div>
            <div class="text-center">+{{ score }}points</div>
          </div>
        </div>

        <div
          v-else-if="
            !qnCorrect &&
            qnAnswered &&
            timer == 0 &&
            !qnNumStore.user_id.includes('Host')
          "
        >
          <div class="grid grid-flow-row grid-col-1 gap-1">
            <div class="flex justify-center mt-24 mb-5">
              <img
                src="../assets/incorrect.png"
                style="width: 170px; height: 175px"
              />
            </div>
            <div class="text-lg font-bold text-center">That's wrong :(</div>
            <div class="text-center">0 points</div>
          </div>
        </div>

        <div
          v-else-if="
            qnAnswered && timer != 0 && !qnNumStore.user_id.includes('Host')
          "
        >
          <div class="grid grid-flow-row grid-col-1 gap-1">
            <div class="flex justify-center mt-24 mb-5">
              <svg
                class="inline mr-2 w-14 h-14 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                viewBox="0 0 100 101"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                  fill="currentColor"
                />
                <path
                  d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                  fill="currentFill"
                />
              </svg>
              <span class="sr-only">Loading...</span>
            </div>
            <div class="text-lg font-bold text-center">
              Waiting for the other team to respond...
            </div>
          </div>
        </div>
        <div v-else>
          <div class="grid grid-flow-row grid-col-1 gap-1 justify-center">
            <div class="text-2xl text-center font-bold mt-8">
              Yay! So who are the leaders?
            </div>
            <!-- just for the host to use -->
            <button class="btn-soloQuiz" @click="moveToScoreboard()">
              Let's go!
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style></style>
