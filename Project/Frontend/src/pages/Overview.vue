<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>
  <v-app>
    <v-container>
      <v-card>
        <v-card-title>Account Information</v-card-title>
        <v-card-text v-if="account">
          <v-list>
            <v-list-item>
                <v-list-item-title>Username:</v-list-item-title>
                <v-list-item-subtitle>{{ account.username }}</v-list-item-subtitle>
            </v-list-item>
            
            <v-list-item>
                <v-list-item-title>Email:</v-list-item-title>
                <v-list-item-subtitle>{{ account.email }}</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <v-list-item-title>Street:</v-list-item-title>
                <v-list-item-subtitle>{{ account.street }}</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <v-list-item-title>House Number:</v-list-item-title>
                <v-list-item-subtitle>{{ account.house_number }}</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <v-list-item-title>Country:</v-list-item-title>
                <v-list-item-subtitle>{{ account.country }}</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <v-list-item-title>Complementary Address:</v-list-item-title>
                <v-list-item-subtitle>{{ account.complementary_address }}</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <v-list-item-title>Telephone Number:</v-list-item-title>
                <v-list-item-subtitle>{{ account.tel_number }}</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <v-list-item-title>Payment Email:</v-list-item-title>
                <v-list-item-subtitle>{{ account.payment_email }}</v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-card-text v-else>
          Not Logged in... <br/>
          Sozzy?
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>

export default {
  data() {
    return {
    };
  },
  mounted() {
    // Fetch account information when the component is mounted
  },
  methods: {
  },
  computed: {
    account() {
      return this.$store.getters.user;
    }
  }
};
</script>

<style scoped>
.Overview {

}
</style>
