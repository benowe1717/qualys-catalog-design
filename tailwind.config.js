/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        'wave-001': "url('./background-image-001.png')",
      }
    },
    colors: {
      red: {
        DEFAULT: '#ed2e26',
      },
      blue: {
        DEFAULT: '#2e8be0',
        700: '#3677c6',
      },
      black: {
        DEFAULT: '#262626',
      },
      slateblue: {
        50: '#edf3f7',
        100: '#dee8f1',
        150: '#dbe6f0',
        DEFAULT: '#9bc0e0',
      },
      gray: {
        DEFAULT: '#6a778b',
      },
      white: {
        DEFAULT: '#f7fafc',
        600: '#edf3f8',
        700: '#dae8f1',
      },
      lightgray: {
        DEFAULT: '#f4f6f8',
      },
      darkblue: {
        400: '#232f43',
        DEFAULT: '#1d2737',
      },
      skyblue: {
        DEFAULT: '#b5d0e5',
      },
      spacegray: {
        400: '#46556d',
        DEFAULT: '#44536b',
        600: '#3c495d',
      },
      foundation: {
        DEFAULT: '#2c75be',
      },
      onboarding: {
        DEFAULT: '#244f75',
      },
      specialist: {
        DEFAULT: '#ed2e26',
      },
    },
  },
  plugins: [],
}

