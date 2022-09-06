import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "flowbite";
import router from "./router/";
import { VueQueryPlugin } from "vue-query";
import { createPinia } from "pinia";

const app = createApp(App);
app.use(router);
app.use(VueQueryPlugin);
app.use(createPinia());
app.mount("#app");
