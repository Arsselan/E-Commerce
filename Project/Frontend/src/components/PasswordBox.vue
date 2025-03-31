<!-- edited by Miles Sasportas-->
<template>

  <v-form class="password-box">
    <v-progress-linear
      :color="score.color"
      :model-value="score.value"
    ></v-progress-linear>
    <br/>
    <v-text-field
      v-model="password"
      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
      :rules="[rules.required, rules.min, rules.strength]"
      validate-on-blur
      :type="showPassword ? 'text' : 'password'"
      label="Passwort"
      class="mb-6"
      @click:append="showPassword = !showPassword"
      variant="outlined"
      density="compact"
    ></v-text-field>
  </v-form>
</template>
<script>
import zxcvbn from 'zxcvbn';

export default  {
  name: 'password-box',
  components: {

  },
  props: {
    modelValue: {
      // type: String,
      required: true,
    }
  },
  mounted () {

  },
  data() { 
    return {
      showPassword: false,
      rules: {
        required: value => !!value || 'Enter a password',
        min: v => v.length >= 8 || 'Use 8 characters or more for your password',
        strength: v => zxcvbn(v).score >= 3 || 'Please choose a stronger password. Try a mix of letters, numbers, and symbols.',
      }
    };
  },
  methods: {

  },
  computed: {
    score() {
      if (!this.modelValue) {
        // Handle the case where the password is undefined or null
        return {
          color: 'grey', // or any other color to indicate no password
          value: 0,
        };
      }

      const result = zxcvbn(this.modelValue);
      
      switch (result.score) {
        case 4:
          return {
            color: "light-blue",
            value: 100
          };
        case 3:
          return {
            color: "light-green",
            value: 75
          };
        case 2:
          return {
            color: "yellow",
            value: 50
          };
        case 1:
          return {
            color: "orange",
            value: 25
          };
        default:
          return {
            color: "red",
            value: 0
          };
      }
    },
    password: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit('update:modelValue', value);
      }
    }
  },
}


</script>

<style scoped>
  .password-box {

  }
</style>
