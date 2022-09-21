<template>
  <div id="Quiz">
    <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
      <div class="p-10 ml-6 mr-6">
        <!--Header-->
        <div class="grid grid-rows-2 grid-flow-col gap-2">
          <div class="text-4xl font-semibold col-span-2">GameVerse</div>
          <div class="text-2xl col-span-2">Quiz Category</div>
          <div class="text-sm row-span-2 flow-root">
            <p class="float-right mt-10">Question {{ qnNum.value + 1 }} of 3</p>
          </div>
        </div>

        <div
          class="h-24 w-screen bg-blue-600/50 -ml-16 mt-2 mb-8 text-center flex justify-center items-center"
        >
          <!-- <div class="text-4xl" v-for="question in store.quiz.questions" :key="question"> -->
          <div class="text-4xl">
            <div>{{store.quiz.questions[qnNum].question}}</div>
          </div>
        </div>


        <div class="grid grid-cols-6 gap-4">
          <div class="col-start-2 col-span-4">
            <form v-if="store.quiz.questions[qnNum]">
              <div
                class="grid grid-rows-2 grid-cols-2 gap-0 place-content-stretch"
              >

                <button
                  class="button h-24 m-2 box-border rounded-lg hover:bg-blue-900"
                  v-for="option,index in store.quiz.questions[qnNum].options"
                  :key="index"
                  :value="option"
                  v-html="option"
                  @click.prevent="checkAnswers(event)"
                ></button>

              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import Quiz from '../services/Quiz'
import {ref, onMounted, onBeforeMount} from 'vue'
import { useQuizCreationStore } from '../stores/quizCreation';

const store = useQuizCreationStore()
const qnNum = ref(0)

onBeforeMount(() => {
  getData();
})

const getData = async () => {
  const response = await Quiz.getQuiz(1)
  store.quiz = response.data
  console.log(store.quiz.questions)
}

function checkAnswers(event) {
  console.log(qnNum.value)
  console.log(store.quiz.questions[qnNum.value])
  var answer_key = store.quiz.questions[qnNum.value].answer
  if (store.quiz.questions[qnNum.value].options[answer_key.value] == event){
    console.log("correct")
  }
  else{
    console.log("wrong lol")
  }
  console.log(qnNum.value)
  return qnNum.value+=1
}


</script>
