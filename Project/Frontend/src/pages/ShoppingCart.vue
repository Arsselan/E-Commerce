<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>
    <section class="shopping-cart">
        <v-card height="100vh">
          <v-card-title>
            Shopping Cart
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row 
                v-for="product in cart"
                :key="product.id"
              >
                <v-col cols="6">
                  <img :src="product.imgpath" :alt="`${product.name}'s image'`">
                </v-col>
                <v-col cols="6">
                  <v-row justify="center" align="center">
                    <span class="productName"> {{ product.name }}</span> 
                    <v-btn
                      class="amount-button amount-button-minus"
                      density="compact"
                      icon="mdi-trash-can"
                      x-small
                      @click="removeProduct(product)"
                    >
                    </v-btn>
                  </v-row>
                  <v-row justify="center" align="center">
                    <v-btn
                      class="amount-button amount-button-minus"
                      density="compact"
                      icon="mdi-minus"
                      x-small
                      :disabled="product.amount == 1"
                      @click="quantityChanged(product, -1)"
                    >
                    </v-btn>
                    <span>
                      {{ product.amount }}
                    </span>
                    <v-btn
                      class="amount-button amount-button-plus"
                      density="compact"
                      icon="mdi-plus"
                      x-small
                      :disabled="product.amount == product.stock"
                      @click="quantityChanged(product, +1)"
                    />
                    <span class="stockText">
                      Stck: {{ product.stock }}
                    </span>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions v-if="showCheckoutButtonComputed">
            <router-link
              to="/checkout"
            >
              <v-btn
                color="primary"
                variant="tonal"
              >
                Bezahlen
              </v-btn>
            </router-link>
          </v-card-actions>
        </v-card>
        
    </section>

</template>


<script>

export default {
  props: {
    showCheckoutButton: {
      required: false,
      default: true,        
    }
  },
    mounted () {

    },
    data () {
      return {
        products: [],
        carct: [{ 
          "id": 1,
            "name": "Product 1!", 
            "desc": "Description 1", 
            "price": 19.99, 
            "stock": 10, 
            "imgpath": "../assets/logo.png",
            amount: 1
          }

        ],
      }
    },
    methods: {
      quantityChanged(product, amount) {
        product.amount += amount;
      },
      removeProduct(product) {
        this.$store.dispatch("removeFromCart", product.id);
      },
    },
    computed: {
      cart() {
        return this.$store.state.cart;
      },
      showCheckoutButtonComputed() {
        return this.$store.state.cart.length > 0 && this.showCheckoutButton;
      },
    },
}


</script>

<style scoped>
.shopping-cart{

  }
  .productName {
    font-size: 14px;
    font-weight: bolder;
  }

  .stockText {
    font-size: 10px;
    font-style: italic;
  }

  .amount-button{
    margin-left: 5px;
    margin-right: 5px;
  }

  .amount-button-plus{
  }
  .amount-button-minus{
  }

</style>
