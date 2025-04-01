<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>
  <div>
    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Account</div>

      <v-text-field
        density="compact"
        placeholder="Email address"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
        v-model="username"
        @keydown.enter="login" 
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Password
      </div>

      <v-text-field
        :append-inner-icon="passwordVisible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="passwordVisible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="passwordVisible = !passwordVisible"
        v-model="password"
        @keydown.enter="login" 
      ></v-text-field>

      <v-btn
        block
        class="mb-8"
        color="primary"
        size="large"
        :disabled="username == '' || password == ''"
        @click="login"
        :loading="loggingIn"
      >
        Log In
      </v-btn>

      <v-card-text class="text-center">
        <router-link to="/Register">
          Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
        </router-link>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import UserService from "../Services/UserService.js";

export default {
  name: 'Login',
  components: {},
  data: () => ({
    passwordVisible: false,
    username: '',
    password: '',
    loggingIn: false,
  }),
  methods: {
    async login() {
      try {
        if (!this.username || !this.password) {
          return;
        }

        this.loggingIn = true;
        await UserService.login(this.username, this.password);
        const user = await UserService.getCurrentUser();
        this.$store.dispatch('updateUser', user);
        this.redirectAndReload("/");
      } catch (error) {
        console.error(error);
        alert("Login failed!");
      } finally {
        this.loggingIn = false;
      }
    },
    //author: Arsselan
    redirectAndReload(path) {
      this.$router.push(path).then(() => {
        window.location.reload();
      });
    },
  },
}
</script>


<style scoped>
/* ... (deine Stile hier) */
</style>
