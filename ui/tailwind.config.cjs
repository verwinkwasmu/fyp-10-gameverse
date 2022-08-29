/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        'quiz':"url('/src/assets/bg.png')",
      },
      fontFamily: {
        'sans':['Poppins'],
      },
    },
  },
  plugins: [],
}
