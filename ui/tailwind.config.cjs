/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        'quiz':"url('/img/bg.png')",
      },
      fontFamily: {
        'sans':['Poppins'],
      },
    },
  },
  plugins: [],
}
