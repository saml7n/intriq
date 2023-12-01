module.exports = {
  mode: 'jit',
  purge: {
    enabled: process.env.NODE_ENV === 'production',
    safeList: [],
    content: ['./index.html', './src/**/*.tsx', './src/**/*.ts'],
  },
  theme: {
    minWidth: {
      '40': '10rem',
      '60': '15rem',
      '80': '20rem',
      '100': '25rem',
    },
    maxWidth: {
      '120': '30rem',
      '160': '40rem',
      '200': '50rem',
    }
  },
  variants: {},
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
		themes: [
			{
				light: {
					"primary": "#2b49ff",
					"secondary": "#00b5b4",
					"accent": "#ff301c",
					"neutral": "#0f1023",
					"base-100": "#fff",
					"base-200": "#f6f7fb",
					"base-300": "#fafbfc",
					"info": "#98d7f0",
					"success": "#9cdcc5",
					"warning": "#e0ca96",
					"error": "#f8bbb0",
				},
			},
			{
				dark: {
					"primary": "#2b49ff",
					"secondary": "#00b5b4",
					"accent": "#ff301c",
					"neutral": "#4e5168",
					"base-100": "#393b51",
					"base-200": "#2b2d43",
					"base-300": "#0f1023",
					"info": "#98d7f0",
					"success": "#9cdcc5",
					"warning": "#e0ca96",
					"error": "#f8bbb0",
				},
			},
		],
	},
}
