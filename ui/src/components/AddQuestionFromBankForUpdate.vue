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
    options: {
      option_1: question.option_1,
      option_2: question.option_2,
      option_3: question.option_3,
      option_4: question.option_4,
    },
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
        <div class="text-5xl font col-span-2">GameVerse Quiz Creation</div>
      </div>
      <div class="mx-auto mt-16 max-w-xl rounded overflow-hidden">
        <div class="flex items-center py-4">
          <div class="w-4/6 flex">
            <p class="text-3xl font col-span-2">Question Bank</p>
          </div>
        </div>
        <div class="flex flex-row">
          <div class="grow">
            <div class="rounded-md shadow">
              <a
                href="#"
                class="flex leading-tight rounded-md border border-transparent bg-blue-900 px-8 py-3 text-base font-medium text-white hover:bg-blue-900 md:py-1 md:px-10"
                >{{ route.params.category }}</a
              >
            </div>
          </div>
        </div>
        <div class="flex flex-row">
          <div class="rounded-md shadow pt-3 basis-1/4">
            <a
              href="#"
              class="flex w-full items-center justify-center rounded-md border border-transparent bg-blue-800 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 md:py-1 md:px-3"
              >Questions: {{ data.length }}</a
            >
          </div>
        </div>
        <div class="text-m row-span-2 flow-root">
          <p class="float-left mt-10">Questions:</p>
        </div>
        <div v-if="isSuccess">
          <div v-for="(question, index) in data" :key="index">
            <div class="text-sm">
              <p>Q{{ index + 1 }}.</p>
            </div>
            <div class="flex flex-row">
              <div class="basis-2/3 pr-3">
                <div class="rounded-md shadow">
                  <a
                    href="#"
                    class="flex w-full items-center justify-left rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 md:py-1 md:px-10"
                  >
                    {{ question.title }}</a
                  >
                </div>
              </div>
              <div class="basis-1/3">
                <div class="rounded-md shadow">
                  <button
                    v-if="
                      !questionBankStore.addedQuestions.includes(question.title)
                    "
                    class="flex w-full items-center justify-center rounded-md border border-transparent bg-cyan-600 px-8 py-3 text-base font-medium text-white hover:bg-cyan-700 md:py-1 md:px-7"
                    @click="addQuestion(question)"
                  >
                    Add Question
                  </button>
                  <button
                    v-else
                    class="flex w-full items-center justify-center rounded-md border border-transparent bg-red-600 px-8 py-3 text-base font-medium text-white hover:bg-red-700 md:py-1 md:px-7"
                    @click="removeQuestion(question.title)"
                  >
                    Remove Question
                  </button>
                </div>
              </div>
            </div>
            <div class="flex flex-row pt-3">
              <div class="basis-1/4 pr-3">
                <div class="rounded-md shadow">
                  <a
                    href="#"
                    class="flex w-full items-center justify-left rounded-md border border-transparent px-8 py-3 text-base font-medium text-white md:py-1 md:px-10"
                    :class="
                      question.answer == 'option_1'
                        ? 'bg-green-500 hover:bg-green-600'
                        : 'bg-blue-900 hover:bg-blue-800'
                    "
                  >
                    {{ question.option_1 }}</a
                  >
                </div>
              </div>
              <div class="basis-1/4 pr-3">
                <div class="rounded-md shadow">
                  <a
                    href="#"
                    class="flex w-full items-center justify-left rounded-md border border-transparent px-8 py-3 text-base font-medium text-white md:py-1 md:px-10"
                    :class="
                      question.answer == 'option_2'
                        ? 'bg-green-500 hover:bg-green-600'
                        : 'bg-blue-900 hover:bg-blue-800'
                    "
                  >
                    {{ question.option_2 }}</a
                  >
                </div>
              </div>
              <div class="basis-1/4 pr-3">
                <div class="rounded-md shadow">
                  <a
                    href="#"
                    class="flex w-full items-center justify-left rounded-md border border-transparent px-8 py-3 text-base font-medium text-white md:py-1 md:px-10"
                    :class="
                      question.answer == 'option_3'
                        ? 'bg-green-500 hover:bg-green-600'
                        : 'bg-blue-900 hover:bg-blue-800'
                    "
                  >
                    {{ question.option_3 }}</a
                  >
                </div>
              </div>
              <div class="basis-1/4">
                <div class="rounded-md shadow">
                  <a
                    href="#"
                    class="flex w-full items-center justify-left rounded-md border border-transparent px-8 py-3 text-base font-medium text-white md:py-1 md:px-10"
                    :class="
                      question.answer == 'option_4'
                        ? 'bg-green-500 hover:bg-green-600'
                        : 'bg-blue-900 hover:bg-blue-800'
                    "
                  >
                    {{ question.option_4 }}</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="flex justify-center pt-10">
          <div class="pr-4 pt-2">
            <router-link
              class="bg-fuchsia-400 hover:bg-fuchsia-300 text-white font-bold py-2 px-4 rounded"
              :to="{path: '/AllQuizQuestionBankForUpdate'}"
              >Back to Question Bank</router-link
            >
          </div>
          <router-link
            class="bg-red-400 hover:bg-red-300 text-black font-bold py-2 px-4 rounded"
            to="/UpdateQuiz"
          >
            Back to Quiz Update
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
