<script setup>
import Quiz from '../services/Quiz'
import {useRoute, useRouter} from 'vue-router'
import {useQuizUpdateStore} from '../stores/quizUpdate'
import {useQuestionBankStore} from '../stores/questionBank'
import {useQuery} from 'vue-query'

const store = useQuizUpdateStore()
const questionBankStore = useQuestionBankStore()
const route = useRoute()

const {isLoading, isError, isFetching, data, error, isSuccess} = useQuery(
  ['questionsByCategory'],
  () => Quiz.getQuestionsByCategory(route.params.category),
  {
    retry: 2,
    cacheTime: 50000,
  },
)

const addQuestion = (question) => {
  const input = {
    question: question.title,
    answer: question.answer,
    timer: question.timer,
    options: {},
  }

  if (question.option_1) {
    input.options['option_1'] = question.option_1
  }
  if (question.option_2) {
    input.options['option_2'] = question.option_2
  }
  if (question.option_3) {
    input.options['option_3'] = question.option_3
  }
  if (question.option_4) {
    input.options['option_4'] = question.option_4
  }

  store.quiz.questions.push(input)
  questionBankStore.addQuestion(question.title)
}

const removeQuestion = (questionTitle) => {
  for (let i = 0; i < store.quiz.questions.length; i++) {
    if (store.quiz.questions[i].question == questionTitle) {
      store.quiz.questions.splice(i, 1)
    }
  }
  questionBankStore.removeQuestion(questionTitle)
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
        <div class="text-2xl col-span-2">
          Question from {{ route.params.category }}
        </div>
      </div>
      <div class="mx-auto mt-16 max-w-xl rounded">
        <div class="grid justify-center">
        <div class="grid grid-flow-col auto-cols-max gap-4">
          <div
            class="w-80 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            Quiz Title
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
          >
            {{ route.params.category }}
          </div>
        </div>
        <div class="grid grid-flow-col auto-cols-max gap-4 pt-4">
          <div
            class="w-80 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            Number of Questions
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
          >
            {{ data.length }}
          </div>
        </div>

        <div class="grid grid-flow-col auto-cols-max gap-4 pt-4">
          <div
            class="w-80 p-4 bg-blue-900 text-white items-center rounded justify-center text-center"
          >
            Category
          </div>
          <div
            class="w-80 p-4 items-center justify-center bg-indigo-700 rounded text-center"
          >
            {{ route.params.category }}
          </div>
        </div>
      </div>
        <div v-if="isSuccess" class="grid justify-center">
          <div class="float-left mt-10 text-2xl font-bold">Questions</div>
          <div v-for="(question, index) in data" :key="index">
            <div class="text-sm pt-4">
              <p>Q{{ index + 1 }}.</p>
            </div>
            <div class="flex grid grid-flow-row auto-rows-max gap-4">
              <div class="grid grid-flow-col auto-cols-max gap-4 w-full">
                <div
                  class="shadow w-96 justify-items-stretch bg-indigo-700 px-8 py-3 mt-6 text-base font-medium text-white"
                >
                  {{ question.title }}
                </div>
                <div
                  class="flex bg-blue-900 px-8 py-3 mt-6 text-base font-medium text-white justify-center items-center"
                >
                  Time: {{ question.timer }}
                </div>
                <div>
                  <button
                    v-if="
                      !questionBankStore.addedQuestions.includes(question.title)
                    "
                    class="grid justify-items-end bg-cyan-600 px-8 py-3 mt-6 text-white hover:bg-cyan-700 rounded-lg"
                    @click="addQuestion(question)"
                  >
                    Add Question
                  </button>
                  <button
                    v-else
                    class="grid justify-items-end bg-red-600 px-8 py-3 mt-6 text-base text-white hover:bg-red-700 rounded-lg"
                    @click="removeQuestion(question.title)"
                  >
                    Remove Question
                  </button>
                </div>
              </div>
              
            </div>

            <div class="flex grid grid-flow-row auto-rows-max gap-4">
              <div
                v-if="question.option_1"
                class="w-full justify-left text-base pt-4 font-medium text-white"
              >
                <div class="grid grid-flow-col auto-cols-max gap-4">
                  <div
                    v-if="question.answer == 'option_1'"
                    class="grid grid-flow-col auto-cols-max gap-4"
                  >
                    <div
                      class="font-bold text-white rounded-full bg-green-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✓
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-green-500"
                    >
                      {{ question.option_1 }}
                    </div>
                  </div>
                  <div v-else class="grid grid-flow-col auto-cols-max gap-4">
                    <div
                      class="font-bold text-white rounded-full bg-red-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✖
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-blue-900"
                    >
                      {{ question.option_1 }}
                    </div>
                  </div>
                </div>
              </div>
              <div
                v-if="question.option_2"
                class="w-full justify-left text-base font-medium text-white"
              >
                <div class="grid grid-flow-col auto-cols-max gap-4">
                  <div
                    v-if="question.answer == 'option_2'"
                    class="grid grid-flow-col auto-cols-max gap-4"
                  >
                    <div
                      class="font-bold text-white rounded-full bg-green-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✓
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-green-500"
                    >
                      {{ question.option_2 }}
                    </div>
                  </div>
                  <div v-else class="grid grid-flow-col auto-cols-max gap-4">
                    <div
                      class="font-bold text-white rounded-full bg-red-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✖
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-blue-900"
                    >
                      {{ question.option_2 }}
                    </div>
                  </div>
                </div>
              </div>
              <div
                v-if="question.option_3"
                class="w-full justify-left text-base font-medium text-white"
              >
                <div class="grid grid-flow-col auto-cols-max gap-4">
                  <div
                    v-if="question.answer == 'option_3'"
                    class="grid grid-flow-col auto-cols-max gap-4"
                  >
                    <div
                      class="font-bold text-white rounded-full bg-green-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✓
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-green-500"
                    >
                      {{ question.option_3 }}
                    </div>
                  </div>
                  <div v-else class="grid grid-flow-col auto-cols-max gap-4">
                    <div
                      class="font-bold text-white rounded-full bg-red-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✖
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-blue-900"
                    >
                      {{ question.option_3 }}
                    </div>
                  </div>
                </div>
              </div>
              <div
                v-if="question.option_4"
                class="w-full justify-left text-base font-medium text-white"
              >
                <div class="grid grid-flow-col auto-cols-max gap-4">
                  <div
                    v-if="question.answer == 'option_4'"
                    class="grid grid-flow-col auto-cols-max gap-4"
                  >
                    <div
                      class="font-bold text-white rounded-full bg-green-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✓
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-green-500"
                    >
                      {{ question.option_4 }}
                    </div>
                  </div>
                  <div v-else class="grid grid-flow-col auto-cols-max gap-4">
                    <div
                      class="font-bold text-white rounded-full bg-red-500 flex items-center justify-center w-12 h-12 align-middle"
                    >
                      ✖
                    </div>
                    <div
                      class="w-full justify-left px-8 py-3 text-base font-medium text-white bg-blue-900"
                    >
                      {{ question.option_4 }}
                    </div>
                  </div>
                </div>
              </div>
              <!-- <div class="basis-1/3 pb-4">
                <div>
                  <button
                    v-if="
                      !questionBankStore.addedQuestions.includes(question.title)
                    "
                    class="grid justify-items-end bg-cyan-600 px-8 py-3 text-white hover:bg-cyan-700 rounded-lg"
                    @click="addQuestion(question)"
                  >
                    Add Question
                  </button>
                  <button
                    v-else
                    class="grid justify-items-end bg-red-600 px-8 py-3 text-base text-white hover:bg-red-700  rounded-lg"
                    @click="removeQuestion(question.title)"
                  >
                    Remove Question
                  </button>
                </div>
              </div> -->
            </div>
          </div>
        </div>

        <div class="flex justify-center pt-10">
          <router-link
            class="btn-return"
            :to="{path: '/AllQuizQuestionBankForUpdate'}"
            >Back to Question Bank</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
