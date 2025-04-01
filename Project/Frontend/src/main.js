// edited by Yannic
// edited by Miles Sasportas
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'

import store from "./store/store.js";

// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// Material icons
import '@mdi/font/css/materialdesignicons.min.css'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },

});

createApp(App)
    .use(router)
    .use(vuetify)
    .use(store)
    .mount('#app')
;