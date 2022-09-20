<template>
  <div id="Quiz">
    <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
      <div class="p-10 ml-6 mr-6">
        <!--Header-->
        <div class="grid grid-rows-2 grid-flow-col gap-2">
          <div class="text-4xl font-semibold col-span-2">GameVerse</div>
          <div class="text-2xl col-span-2">Quiz Category</div>
          <div class="text-sm row-span-2 flow-root">
            <p class="float-right mt-10">Question {{ index + 1 }} of 3</p>
          </div>
        </div>

        <!-- <div
          class="h-24 w-screen bg-blue-600/50 -ml-16 mt-2 mb-8 text-center flex justify-center items-center"
        >
          <div class="text-4xl">
            <div
              v-html="isLoading ? 'Loading...' : currentQuestion.question"
            ></div>
          </div>
        </div>

        <div class="grid grid-cols-6 gap-4">
          <span class="font-mono text-5xl countdown">
            <span id="countdowntimer">15</span>
          </span>

          <div class="col-start-2 col-span-4 mb-6">
            <img
              class="card rounded-lg object-fill w-full h-64 flex"
              src="https://images.unsplash.com/photo-1543158015-04650a9d832a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2833&q=80"
            />
          </div>
        </div>

        <div class="grid grid-cols-6 gap-4">
          <div class="col-start-2 col-span-4">
            <form v-if="currentQuestion">
              <div
                class="grid grid-rows-2 grid-cols-2 gap-0 place-content-stretch"
              >
                <button
                  class="button h-24 m-2 box-border rounded-lg hover:bg-blue-900"
                  v-for="answer in currentQuestion.answers"
                  :index="currentQuestion.key"
                  :key="answer"
                  v-html="answer"
                  @click.prevent="ButtonClick"
                ></button>
              </div>
            </form>
          </div>
        </div> -->

        <!-- <div class="loader" v-if="isLoading" message="Answer's locked in! Waiting for all players">
          <div role="status">
            <svg class="inline mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-gray-600 dark:fill-gray-300" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
          </div>
      </div> -->
      </div>
    </div>
  </div>
</template>

<!-- <script type="text/javascript">
import axios from "axios";
var timeleft = 15;
var downloadTimer = setInterval(function () {
  timeleft--;
  document.getElementById("countdowntimer").textContent = timeleft;
  if (timeleft <= 0)
    clearInterval(downloadTimer);
}, 1000);


export default {
  name: "Quiz",
  data() {
    return {
      isLoading: true,
      questions: [],
      index: 0
    };
  },
  computed: {
    currentQuestion() {
      if (this.questions !== []) {
        return this.questions[this.index];
      }
      return null;
    }
  },
  methods: {
    async fetchQuestions() {
      this.isLoading = true;
      let response = await fetch("https://opentdb.com/api.php?amount=10&category=9");
      let jsonResponse = await response.json();
      let index = 0;
      let data = jsonResponse.results.map((question) => {
        question.answers = [
          question.correct_answer,
          ...question.incorrect_answers,
        ];
        // shuffle questions.answers array
        for (let i = question.answers.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [question.answers[i], question.answers[j]] = [
            question.answers[j],
            question.answers[i],
          ];
        }
        // add rightAnswer and key property to each question
        question.rightAnswer = null;
        question.key = index;
        index++;
        return question;

      });
      this.questions = data;
      this.isLoading = false;

    },
    ButtonClick: function (event) {
      /* Find index to identiy question object in data */
      let index = event.target.getAttribute("index");

      let pollutedUserAnswer = event.target.innerHTML; // innerHTML is polluted with decoded HTML entities e.g ' from &#039;
      /* Clear from pollution with ' */
      let userAnswer = pollutedUserAnswer.replace(/'/, "&#039;");

      /* Set userAnswer on question object in data */
      this.questions[index].userAnswer = userAnswer;

      /* Set class "clicked" on button with userAnswer -> for CSS Styles; Disable other sibling buttons */
      event.target.classList.add("clicked");
      let allButtons = document.querySelectorAll(`[index="${index}"]`);

      for (let i = 0; i < allButtons.length; i++) {
        if (allButtons[i] === event.target) continue;

        allButtons[i].setAttribute("disabled", "");
      }

      /* Invoke checkAnswer to check Answer */
      this.checkAnswer(event, index);
    },
    checkAnswer: function (event, index) {
      let question = this.questions[index];

      if (question.userAnswer) {
        if (this.index < this.questions.length - 1) {
          setTimeout(
            function () {
              this.index += 1;
            }.bind(this),
            3000
          );
        }
        if (question.userAnswer === question.correct_answer) {
          /* Set class on Button if user answered right, to celebrate right answer with animation joyfulButton */
          event.target.classList.add("rightAnswer");
          /* Set rightAnswer on question to true, computed property can track a streak out of 10 questions */
          this.questions[index].rightAnswer = true;
        } else {
          /* Mark users answer as wrong answer */
          event.target.classList.add("wrongAnswer");
          this.questions[index].rightAnswer = false;
          /* Show right Answer */
          let correctAnswer = this.questions[index].correct_answer;
          let allButtons = document.querySelectorAll(`[index="${index}"]`);
          allButtons.forEach(function (button) {
            if (button.innerHTML === correctAnswer) {
              button.classList.add("showRightAnswer");
            }
          });
        }
      }
    },
  },


  mounted() {
    this.fetchQuestions();
  }
}

</script> -->

<script setup>
import Quiz from '../services/Quiz'
import {ref, onMounted} from 'vue'

const quiz = ref()

onMounted(() => {
  getData()
})

const getData = async () => {
  const response = await Quiz.getQuiz(1)
  quiz.value = response.data
  console.log(quiz.value)
}
</script>
