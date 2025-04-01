<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<!--logout edited by Wael Hourani-->
<template>
  <v-app>
    <v-app-bar dark>
      <router-link to="/">
        <img src="./assets/logo.png" alt="na logo!" :height="85" > 
      </router-link>
      <v-spacer/>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <searchbar/>
      
      <v-spacer/>

      <div v-if="!account">
        <router-link to="/register">
          <span class="register-login-text">
            Register
          </span> 
        </router-link>
        /
        <router-link to="/login">
          <span class="register-login-text">
            Login
          </span> 
        </router-link>
      </div>
    <div v-else>
      <v-btn @click="logout" text>
        <v-icon>
          mdi-logout
        </v-icon>
        <span class="register-login-text">
          Logout
        </span>
      </v-btn>
     </div>

      <v-spacer/>
      <!-- <shopping-cart-icon
        v-if="false"
        @click="showCart = !showCart"
      /> -->
      <v-btn
        @click="showCart = !showCart"
        variant="outlined"
      >
        <img src="./assets/cart-smoll.jpg" alt="" > 
      </v-btn>
    </v-app-bar>
    
    

    <!-- Centered router-view using Vuetify layout and grid system -->
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col>
          <router-view/>
        </v-col>
      </v-row>
    </v-container>

    <left-navigational-drawer>

    </left-navigational-drawer>
    

    <v-navigation-drawer
        v-model="showCart"
        location="right"
        width="40%"
      >
        <shopping-cart/>
      </v-navigation-drawer>


    <!-- Just during development  -->
    <div v-if="isDevelopment">
      <routes-list/>
    </div>

    
  </v-app>
</template>

<script>
import Searchbar from './components/Searchbar.vue'
//import ShoppingCartIcon from './components/ShoppingCartIcon.vue'
import RoutesList from './development/RoutesList.vue'
import ShoppingCart from './pages/ShoppingCart.vue'
import LeftNavigationalDrawer from './components/LeftNavigationalDrawer.vue'
import UserService from './Services/UserService.js'


export default {
  name: 'App',
  components: {
    Searchbar,
    RoutesList,
    ShoppingCart,
    LeftNavigationalDrawer,
    //ShoppingCartIcon
  },
  data() {
    return {
      isDevelopment: false,
      showCart: false,
    }
  },
  methods: {
    async logout() {
  try {
    // Call the logout method from your UserService
    await UserService.logout();

    // Set user state to null
    this.$store.state.user = null; // Modify this based on your Vuex store structure

    // Optional: Redirect to login page after logout
    this.$router.push('/login');
  } catch (error) {
    console.error('Error during logout:', error);
  }
    },
  },
  computed: {
    account() {
      return this.$store.getters.user;
    }
  },
  mounted() {
  },
	beforeCreate() {
		this.$store.commit('initialiseStore');
	}
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.register-login-text {
  font-style: italic;
  font-size: smaller;
  margin-left: 5px;
  margin-right: 5px;
}
</style>

