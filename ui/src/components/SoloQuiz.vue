<template>
  <div id="Quiz">
    <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
      <div class="p-10 ml-6 mr-6">
        <!--Header-->
        <div class="grid grid-rows-2 grid-flow-col gap-2">
          <div class="text-4xl font-semibold col-span-2">GameVerse</div>
          <div class="text-2xl col-span-2">{{store.quiz.category}}</div>
          <div v-if="!qnAnswered" class="text-sm row-span-2 flow-root">
            <p class="float-right mt-10">Question {{ qnNumStore.qnNum + 1 }} of 3</p>
          </div>
        </div>


        <div v-if="!qnAnswered">

          <div class="h-24 w-screen bg-blue-600/50 -ml-16 mt-2 mb-8 text-center flex justify-center items-center">
            <div class="text-4xl">
              <div>{{store.quiz.questions[qnNumStore.qnNum].question}}</div>
            </div>
          </div>


          <div class="grid grid-cols-6 gap-4">

            <span class="font-mono text-5xl countdown">
              {{timer}}
            </span>

            <div class="col-start-2 col-span-4">
              <div class="grid grid-rows-2 grid-cols-2 gap-0 place-content-stretch">

                <button class="button h-24 m-2 box-border rounded-lg hover:bg-blue-900"
                  v-for="option,index in store.quiz.questions[qnNumStore.qnNum].options" :key="index" :value="option"
                  v-html="option" @click="checkAnswers(option)"></button>

              </div>
            </div>
          </div>
        </div>

        <div v-else-if="qnCorrect && qnAnswered">
          <div class="grid grid-flow-row grid-col-1 gap-1">
            <div class="flex justify-center mt-24 mb-5">
              <img src="../assets/correct.png" style="width: 170px; height: 175px" />
            </div>
            <div class="text-lg font-bold text-center">That's correct!</div>
            <div class="text-center">+10 points</div>
          </div>
        </div>

        <div v-else-if="!qnCorrect && qnAnswered">
          <div class="grid grid-flow-row grid-col-1 gap-1">
            <div class="flex justify-center mt-24 mb-5">
              <img src="../assets/incorrect.png" style="width: 170px; height: 175px" />
            </div>
            <div class="text-lg font-bold text-center">That's wrong :(</div>
            <div class="text-center">0 points</div>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>


<script setup>
import Quiz from '../services/Quiz'
import { ref, onMounted, onBeforeMount } from 'vue'
import { useQuizCreationStore } from '../stores/quizCreation';
import { useQnNumberStore } from '../stores/qnNumber';
import ScoreboardVue from './Scoreboard.vue';
import { useRouter, useRoute } from "vue-router";

const route = useRoute();
const client_id = Date.now();

//TODO get actual ids properly
const connection = new WebSocket(
  `ws://localhost:8080/ws/${route.params.room_id}/${client_id}`
);

connection.onopen = () => {
  console.log("connection established");
};

connection.onmessage = (event) => {
  console.log(JSON.parse(event.data))
};

const store = useQuizCreationStore()
const qnNumStore = useQnNumberStore()
const qnCorrect = ref(null)
const qnAnswered = ref(false)
const timer = ref()


onBeforeMount(() => {
  getData();

})

onMounted(() => {
  timer.value = store.quiz.questions[qnNumStore.qnNum].timer
  console.log(timer.value)

  setTimeout(checkAnswers, timer.value * 1000)

  var timerCountdown = setInterval(() => {
    timer.value--
    if (timer.value == 0) {
      clearInterval(timerCountdown)
    }
  }, 1000)
})

const getData = async () => {
  const response = await Quiz.getQuiz(1)
  store.quiz = response.data
  console.log(store.quiz.questions)
}

function checkAnswers(event) {

  if (event == null) {
    event = ""
  }

  var answer_key = store.quiz.questions[qnNumStore.qnNum].answer
  // console.log(answer_key)
  console.log(store.quiz.questions[qnNumStore.qnNum].timer)

  if (store.quiz.questions[qnNumStore.qnNum].options[answer_key] == event) {
    qnCorrect.value = true
    qnAnswered.value = true
    qnNumStore.score += 10
    console.log("correct")
  }
  else {
    qnCorrect.value = false
    qnAnswered.value = true
    console.log("wrong lol")
  }
  console.log(qnNumStore.score)

  const response = {
    'command': 'Done',
    'name': 'Andrew',
    'user_id': client_id,
    'score': qnNumStore.score
  }
  connection.send(JSON.stringify(response));
  return qnNumStore.qnNum += 1
}

</script>