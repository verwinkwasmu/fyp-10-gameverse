<script setup>
import {useRouter} from 'vue-router'
import {useQuizUpdateStore} from '../stores/quizUpdate'
const store = useQuizUpdateStore()
</script>

<template>
  <form
    class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white overflow-auto"
    action="/UpdateQuizSummary"
  >
    <!--Header-->
    <div
      class="grid grid-rows-2 grid-flow-col gap-2 px-10 pt-10 pb-5 ml-6 mr-6"
    >
      <router-link to="/">
        <div class="text-5xl font-semibold col-span-2">GameVerse</div>
      </router-link>
      <div class="text-2xl col-span-2">Updating Quiz</div>
    </div>

    <div
      className="flex flex-wrap lg:flex-nowrap justify-center mx-8 px-8 mb-8"
    >
      <div class="grid grid-cols-1 gap-8 justify-items-center w-8/12 px-4">
        <div class="w-full">
          <label
            for="first_name"
            class="block mb-2 text-xl font-medium text-white"
            >Quiz Category</label
          >
          <input
            type="text"
            id="first_name"
            class="bg-indigo-700 border border-indigo-600 text-white text-sm rounded-lg block w-full p-2.5"
            placeholder="Enter the Quiz Category"
            v-model="store.quiz.category"
            required
          />
        </div>
        <div class="w-full">
          <label
            for="first_name"
            class="block mb-2 text-xl font-medium text-white"
            >Quiz Title</label
          >
          <input
            type="text"
            id="first_name"
            class="bg-indigo-700 border border-indigo-600 text-white text-sm rounded-lg block w-full p-2.5"
            placeholder="Enter the Quiz Name"
            v-model="store.quiz.title"
            required
          />
        </div>
        <div class="w-full">
          <label
            for="first_name"
            class="block -mb-4 text-xl font-medium text-white"
            >Questions</label
          >
        </div>
        <div
          v-for="(question, index) in store.quiz.questions"
          class="w-full p-6 rounded-lg border"
          :key="index"
        >
          <div class="w-full my-5">
            <label
              for="first_name"
              class="block mb-2 text-sm font-medium text-white"
              >Quiz Question {{ index + 1 }}</label
            >
            <input
              type="text"
              id="first_name"
              class="bg-indigo-700 border border-indigo-600 text-white text-sm rounded-lg block w-full p-2.5"
              placeholder="Enter the question name"
              v-model="question.question"
              required
            />
          </div>
          <div class="w-full my-5">
            <div class="grid grid-flow-col">
              <div class="block mb-2 text-sm font-medium text-white">
                Question Timer (in seconds):
              </div>
              <div class="flex items-center mb-4">
                <input
                  :id="'timer-5s-' + index"
                  type="radio"
                  :value="5"
                  :name="'radio-group-' + index"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                  v-model="question.timer"
                  required
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-white dark:text-gray-300"
                  >5</label
                >
              </div>
              <div class="flex items-center mb-4">
                <input
                  :id="'timer-10s' + index"
                  type="radio"
                  :value="10"
                  :name="'radio-group-' + index"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                  v-model="question.timer"
                  required
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-white dark:text-gray-300"
                  >10</label
                >
              </div>
              <div class="flex items-center mb-4">
                <input
                  :id="'timer-15s' + index"
                  type="radio"
                  :value="15"
                  :name="'radio-group-' + index"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                  v-model="question.timer"
                  required
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-white dark:text-gray-300"
                  >15</label
                >
              </div>
              <div class="flex items-center mb-4">
                <input
                  :id="'timer-20s' + index"
                  type="radio"
                  :value="20"
                  :name="'radio-group-' + index"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                  v-model="question.timer"
                  required
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-white dark:text-gray-300"
                  >20</label
                >
              </div>
            </div>
          </div>
          <div
            class="w-full my-5"
            v-for="(value, propertyName, index) in question.options"
            :key="index"
          >
            <div class="flex items-center">
              <label class="block mb-2 text-sm font-medium text-white"
                >Add answer {{ index + 1 }}</label
              >
            </div>
            <input
              type="text"
              class="bg-indigo-700 border border-indigo-600 text-white text-sm rounded-lg block w-full p-2.5"
              placeholder="Enter your option"
              v-model="question.options[propertyName]"
              required
            />
          </div>
          <div class="w-full my-5">
            <div class="grid grid-cols-2">
              <button
                v-if="Object.keys(question.options).length < 4"
                type="button"
                @click="store.addOption(question.options)"
                class="text-blue-400 underline hover:font-bold font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center"
              >
                <svg
                  class="w-6 h-6"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                  ></path>
                </svg>
                Add more answers
              </button>
              <button
                type="button"
                v-if="Object.keys(question.options).length > 1"
                @click="store.removeOption(question.options)"
                class="text-red-600 underline hover:font-bold font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center"
              >
                <svg
                  class="w-6 h-6"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M20 12H4"
                  ></path>
                </svg>
                Remove last answer
              </button>
            </div>
          </div>
          <div>
            <label class="block mb-2 text-sm font-medium text-white"
              >Correct Answer</label
            >
            <!-- 
              TODO gotta find a way to select the answer when it is added from the question bank
              -->
            <select
              v-model="question.answer"
              class="bg-indigo-700 border border-indigo-600 text-white text-sm rounded-lg block w-full p-2.5"
              required
            >
              <option disabled hidden value="">Select your option</option>
              <option
                v-for="(value, propertyName, index) in question.options"
                :key="index"
                :value="propertyName"
              >
                {{ value }}
              </option>
            </select>
          </div>
          <div class="justify-self-end">
            <button
              type="button"
              @click="store.removeQuestion(store.quiz.questions, index)"
              class="text-red-600 bg-slate-200 hover:bg-slate-400 text-sm rounded-lg px-5 py-2.5 text-center inline-flex items-center my-5 h-1/2"
            >
              <span class="text-2xl font-bold">🗑</span> &nbsp; Delete Question
            </button>
          </div>
        </div>
        <div class="w-full">
          <button
            v-if="store.quiz.questions.length < 15"
            type="button"
            @click="store.addQuestion()"
            class="btn-add rounded-lg text-sm px-5 py-2.5 mr-5 mb-2"
          >
            Add Question
          </button>
          <router-link to="/AllQuizQuestionBankForUpdate" tag="button">
            <button
              type="button"
              class="btn-add rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"
            >
              Add from Question Bank
            </button>
          </router-link>
        </div>
      </div>
    </div>
    <div className="">
      <hr class="border-1 border-slate-300" />
      <div class="flex grid grid-cols-1 gap-8 justify-items-center m-5 w-11/12">
        <div>
          <router-link to="/MyQuizzes">
            <button
              type="button"
              class="btn-return"
            >
              Return
            </button>
          </router-link>
          <input
            type="submit"
            class="btn-complete"
            value="Complete Quiz Update"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<style>
body {
  background-image: url('../assets/bg.png');
}
</style>
