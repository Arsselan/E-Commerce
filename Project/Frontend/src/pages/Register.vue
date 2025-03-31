<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>  
  <v-card
    class="mx-auto pa-12 pb-8"
    elevation="8"
    max-width="548"
    rounded="lg"
  >
    <v-stepper
      v-model="step"
      vertical
      :items="stepperItems"
      :loading="true"
    >
      <template v-slot:item.1>
        <v-card-title>Konto Typ</v-card-title>
        <v-card-text>
          <v-radio-group v-model="accountTyp">
            <v-radio label="Käufer-Konto" value="buyer"></v-radio>
            <v-radio label="Verkäufer-Konto" value="seller"></v-radio>
        </v-radio-group>
        </v-card-text>
      </template>

      <template v-slot:item.2>
        <v-card-title>Account Information</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="registerAndProceed">
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="email" 
              label="Email-Addresse"
              required
              @blur="verifiyMail"
              ></v-text-field>
            <password-box v-model="password"></password-box>
          </v-form>
        </v-card-text>
      </template>

      <template v-slot:item.3>
        <v-card-title>Account Information</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="registerAndProceed">
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="last_name" 
              :label="isSeller ? 'Inhaber Name' : 'Name'" 
              required
            ></v-text-field>
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="first_name" 
              :label="isSeller ? 'Inhaber Vorname' : 'Vorname'" 
              required
            ></v-text-field>

            <v-text-field
              v-if="isSeller"
              variant="outlined"  
              density="compact"
              v-model="shopName" 
              label="Shopname" 
              required
            ></v-text-field>
            
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="street" 
              label="Straße" 
              required
            ></v-text-field>
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="house_number" 
              label="Haus-Nummer und Zusatz" 
              required
            ></v-text-field>
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="country" 
              label="Land" 
              required
            ></v-text-field>
            <!-- <v-text-field
                variant="outlined"  
                density="compact"
                v-model="complementary_address" 
                label="Complementary address"
                >
            </v-text-field> -->
            <v-text-field
              variant="outlined"  
              density="compact"
              v-model="tel_number" 
              label="Telefonnummer" 
              required
            ></v-text-field>
            <!-- <v-text-field
                variant="outlined"  
                density="compact"
                v-model="payment_email" 
                label="Email for 
                payme
              nt" placeholder="Only if different than Registration Email" ></v-text-field> -->
            <v-btn 
              :disabled="disableSave"
              type="submit"
              color="primary"
            >
              Account Anlegen
            </v-btn>
          </v-form>
        </v-card-text>
      </template>
    </v-stepper>

    <v-snackbar
      v-model="snackbar"
      :color="snackbarColor"
      multi-line
    >
      {{ snackbarMessage }}
    </v-snackbar>
  </v-card>
</template>

<script>
import PasswordBox from "@/components/PasswordBox.vue";
import UserService from "../Services/UserService.js";

export default {
  name: "register",
  components: {
    PasswordBox,
  },
  data() {
    return {
      accountTyp: "buyer",
      first_name: "",
      last_name: "",
      shopName: '',
      email: '',
      password: '',
      street: '',
      house_number: '',
      country: '',
      complementary_address: '',
      tel_number: '',
      payment_email: '',
      snackbar: false,
      snackbarMessage: "",
      snackbarColor: "",
      step: 1,
      stepperItems: [
        'Typ',
        'Login Daten',
        'Adressdaten ',
      ],
    };
  },
  methods: {
    createUser() {
      return {
          password: this.password,
          
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          username: this.isSeller ? this.shopName : this.email,
          bio: '',

          street: this.street,
          house_number: this.house_number,
          country: this.country,
          telnumber: this.tel_number,

          is_buyer: !this.isSeller,
          is_seller: this.isSeller,

          // Derzeit nicht angzeigt
          complement_adress: this.complementary_address,
          email_paiement: this.payment_email,
      };
    },
    async registerAndProceed() {
      try {
        // Call the UserService register function with data for the current step
        const user = await UserService.register(this.createUser());

        this.showSnackbar("Erfolgreich registriert!", "success");
        this.$store.dispatch('updateUser', user);
        this.$router.push("/");
      } catch (error) {
        console.error(error);
        // Show failure message
        
        this.showSnackbar("Registrierung Fehlgeschalgen!\n" + JSON.stringify(error.response.data), "error");
      }
    },
    showSnackbar(message, color) {
      this.snackbar = true;
      this.snackbarMessage = message;
      this.snackbarColor = color;
    },
  
    getDataForStep(step) {
      // Get data for the current step
      switch (step) {
        case 1:
          return { username: this.username, email: this.email, password: this.password };
        case 2:
          return {
            street: this.street,
            house_number: this.house_number,
            country: this.country,
            complementary_address: this.complementary_address,
            tel_number: this.tel_number,
            payment_email: this.payment_email,
          };
        default:
          return {};
      }
    },

    async verifiyMail() {
      try {
        if(!await UserService.verifyMail(this.email)){
          this.showSnackbar(`E-Mail ${this.email} bereits benutzt!`);
          this.email = "";
        }
      } catch (error) {
        if (error.response && error.response.status === 404) {
          this.showSnackbar("Endpunkt noch ned implementiert")
          return;
        }

        console.error(error);
        this.showSnackbar("E-Mail adresse kann nicht verwendet werden.\n" + JSON.stringify(error?.response?.data), "error");
        // Ist nicht user-freundlich aber bei diesem Studenten Projekt... EJAAL
        this.email = "";
      }
    }
  },
  computed: {
    isSeller() {
      return this.accountTyp == 'seller';
    },
    disableSave() {
      return this.accountTyp == "" 
        || this.first_name == ""
        || this.last_name == ""
        || (this.isSeller && this.shopName == "")
        || this.email == ""
        || this.password == ""
        || this.street == ""
        || this.house_number == ""
        || this.country == ""
        || this.tel_number == ""

        // || this.complementary_address == ""
        // || this.payment_email == ""
      ;
    },
  }
};
</script>

<style scoped>

</style>
