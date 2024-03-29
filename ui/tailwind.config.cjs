/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors')

module.exports = {
  darkMode: "class",
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      backgroundImage: {
        quiz: "url('/src/assets/bg.png')",
      },
      fontFamily: {
        sans: ["Poppins"],
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
