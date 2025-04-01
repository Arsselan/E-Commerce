<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>
  <v-navigation-drawer
    v-if="user"
    :rail="rail"
    permanent
    @click="rail = false"
    class="left-drawer"
  >
    <v-list-item
      :prepend-avatar="`https://randomuser.me/api/portraits/men/${user.id}.jpg`"
      :title="user.username"
      nav
    >
      <template v-slot:append>
        <v-btn
          variant="text"
          icon="mdi-chevron-left"
          @click.stop="rail = !rail"
        ></v-btn>
      </template>
    </v-list-item>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <router-link to="/">
        <v-list-item prepend-icon="mdi-home-city" title="Home" value="home"></v-list-item>
      </router-link>
      <router-link to="/account">
        <v-list-item prepend-icon="mdi-account" title="My Account" value="account"></v-list-item>
      </router-link>
      <router-link to="/orders">
        <v-list-item prepend-icon="mdi-package" title="My Orders" value="orders"></v-list-item>
      </router-link>
      <router-link v-if="user.is_seller" to="/?&seller=1">
        <v-list-item prepend-icon="mdi-package-variant" title="My Products" value="products"></v-list-item>
      </router-link>
      <router-link v-if="user.is_seller" to="/upload">
        <v-list-item prepend-icon="mdi-plus" title="Add Product" value="add-product"></v-list-item>
      </router-link>
      <router-link to="/favorite">
        <v-list-item prepend-icon="mdi-heart" title="Favorite" value="favorite"></v-list-item>
      </router-link>
    </v-list>
  </v-navigation-drawer>
</template>


<script lang="js">
import UserService from '@/Services/UserService';


  export default  {
    name: 'left-navigational-drawer',
    props: {
      // user: {
      //   requried: false,
      //   default: {
      //     name: "Hans Franz",
      //     isSeller: false,
      //   }
      // },
    },
    async mounted () {
      try {
        const user = await UserService.getCurrentUser();
        this.$store.dispatch('updateUser', user);
      }
      catch(error) {
        console.log("Nicht eingeloggt", error);
      }
    },
    data () {
      return {
        rail: true,

      }
    },
    methods: {

    },
    computed: {
      user() {
        return this.$store.getters.user;
      }

    }
}


</script>


<style scoped>
.left-drawer {
  z-index: 1; /* Set a higher z-index */
}
</style>