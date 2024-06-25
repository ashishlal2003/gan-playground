// tailwind.config.js

module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        'ibm-plex-sans': ['"IBM Plex Sans"', 'sans-serif'],
      },
      fontSize: {
        '72': '72px',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
