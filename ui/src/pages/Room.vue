<script setup>
import Quiz from "../services/Quiz";
import { useQuery } from "vue-query";

const { isLoading, isError, isFetching, data, error, refetch } = useQuery(
  "quizzes",
  Quiz.getQuizzes
);

console.log(data);
</script>

<template lang="">
  <div>
    <div v-if="isLoading">Loading...</div>
    <div v-else-if="isError">An error has occured {{ error }}</div>
    <div v-else-if="data">
      {{ data }}
    </div>
  </div>
</template>

<style lang=""></style>
