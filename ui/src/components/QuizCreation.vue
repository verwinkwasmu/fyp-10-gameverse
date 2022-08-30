<script setup>
import { ref } from "vue";

let quizObject = ref({
  title: "",
  category: "",
  questions: [
    {
      question: "",
      options: {
        option_1: "",
        option_2: "",
      },
      answer: "",
      timer: "",
    },
  ],
});

const addOption = (object) => {
  let i = Object.keys(object).length;
  object[`option_${i + 1}`] = "";
};

const removeOption = (object) => {
  let i = Object.keys(object).length;
  delete object[`option_${i}`];
};

// is there a max question?
const addQuestion = (object) => {
  let newQuestion = {
    question: "",
    options: {
      option_1: "",
    },
    answer: "",
    timer: "",
  };
  object.push(newQuestion);
};

const removeQuestion = (object) => {
  object.pop();
};
</script>

<template>
  <div class="mt-12">
    <p class="flex justify-left text-5xl text-white pt-10 pl-20 font-light">
      Gameverse Quiz Creation
    </p>
    <div className="flex flex-wrap lg:flex-nowrap justify-center m-8 p-8">
      <div class="grid grid-cols-1 gap-8 justify-items-center w-7/12 px-10">
        <div class="w-full">
          <label
            for="first_name"
            class="block mb-2 text-xl font-medium text-white"
            >Quiz Category</label
          >
          <input
            type="text"
            id="first_name"
            class="bg-indigo-700 border border-indigo-600 text-gray-900 text-sm rounded-lg block w-full p-2.5"
            placeholder="Enter the Quiz Category"
            required
          />
        </div>
        <div class="w-full">
          <label
            for="first_name"
            class="block mb-2 text-xl font-medium text-white"
            >Quiz Name</label
          >
          <input
            type="text"
            id="first_name"
            class="bg-indigo-700 border border-indigo-600 text-gray-900 text-sm rounded-lg block w-full p-2.5"
            placeholder="Enter the Quiz Name"
            required
          />
        </div>
        <div v-for="(question, index) in quizObject.questions" class="w-full">
          <div class="w-full my-5">
            <label
              for="first_name"
              class="block mb-2 text-sm font-medium text-white"
              >Quiz Question {{ index + 1 }}</label
            >
            <input
              type="text"
              id="first_name"
              class="bg-indigo-700 border border-indigo-600 text-gray-900 text-sm rounded-lg block w-full p-2.5"
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
                  id="default-radio-1"
                  type="radio"
                  value=""
                  name="default-radio"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >5</label
                >
              </div>
              <div class="flex items-center mb-4">
                <input
                  id="default-radio-1"
                  type="radio"
                  value=""
                  name="default-radio"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >10</label
                >
              </div>
              <div class="flex items-center mb-4">
                <input
                  id="default-radio-1"
                  type="radio"
                  value=""
                  name="default-radio"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >15</label
                >
              </div>
              <div class="flex items-center mb-4">
                <input
                  id="default-radio-1"
                  type="radio"
                  value=""
                  name="default-radio"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                />

                <label
                  for="default-checkbox"
                  class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >20</label
                >
              </div>
            </div>
          </div>
          <div
            class="w-full my-5"
            v-for="(value, propertyName, index) in question.options"
          >
            <label
              for="first_name"
              class="block mb-2 text-sm font-medium text-white"
              >Option {{ index + 1 }}</label
            >
            <input
              id="default-checkbox"
              type="checkbox"
              value=""
              class="w-4 float-right text-indigo-600 bg-gray-100 rounded border-gray-300 mr-20"
            />
            <input
              type="text"
              id="first_name"
              class="bg-indigo-700 border border-indigo-600 text-gray-900 text-sm rounded-lg block w-8/12 p-2.5"
              placeholder="Enter your option"
              required
            />
          </div>
          <div class="w-full my-5">
            <div class="grid grid-cols-2">
              <div class="inline-flex">
                <button
                  v-if="Object.keys(question.options).length < 4"
                  type="button"
                  @click="addOption(question.options)"
                  class="text-white bg-teal-300 hover:bg-teal-400 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-5 my-5 h-1/2"
                >
                  Add Option
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
                </button>
                <button
                  type="button"
                  v-if="Object.keys(question.options).length > 1"
                  @click="removeOption(question.options)"
                  class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center m-5 h-1/2"
                >
                  Remove Option
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
                </button>
              </div>
              <div class="justify-self-end">
                <button
                  type="button"
                  @click="removeQuestion(quizObject.questions)"
                  class="text-red-600 w-8/12 bg-slate-100 hover:bg-slate-200 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center m-5 h-1/2"
                >
                  Remove Question
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
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="w-full">
          <button
            v-if="quizObject.questions.length < 15"
            type="button"
            @click="addQuestion(quizObject.questions)"
            class="text-white bg-cyan-700 hover:bg-cyan-800 font-medium rounded-lg text-sm px-5 py-2.5 mr-5 mb-2"
          >
            Add Question
          </button>
          <button
            type="button"
            class="text-white bg-purple-800 hover:bg-purple-900 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"
          >
            Add from Question Bank
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
