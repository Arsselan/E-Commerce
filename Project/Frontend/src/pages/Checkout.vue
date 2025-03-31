<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>
  <section class="checkout">
    <v-container fluid fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6">
          <v-card class="max-width-card">
            <v-stepper
              v-model="step"
              :items="items"
              show-actions
            >
              <template v-slot:item.1>
                <h3 class="text-h6">Bestellung</h3>

                <br>

                <v-sheet border>
                  <shopping-cart
                    :showCheckoutButton="false"
                  />
                </v-sheet>
              </template>

              <template v-slot:item.2>
                <h3 class="text-h6">Lieferung</h3>

                <br>

                <v-radio-group v-model="shipping" label="Lieferart">
                  <v-radio label="Standard 5€" value="5"></v-radio>
                  <v-radio label="Priorität 10€" value="10"></v-radio>
                  <v-radio label="Selber Tag 20€" value="20"></v-radio>
                </v-radio-group>
              </template>

              <template v-slot:item.3>
                <h3 class="text-h6">Bestätigen</h3>

                <br>

                <v-sheet border>
                  <v-table>
                    <thead>
                      <tr>
                        <th>Artikel</th>
                        <th class="text-end">Anzahl</th>
                        <th class="text-end">Preis</th>
                      </tr>
                    </thead>

                    <tbody>
                      <tr v-for="(product, index) in cart" :key="index">
                        <td v-text="product.name"></td>
                        <td class="text-end" v-text="product.amount"></td>
                        <td class="text-end" v-text="`€ ${product.amount * product.price}`"></td>
                      </tr>

                      <tr>
                        <td>Versand</td>
                        <td></td>
                        <td class="text-end" v-text="`€ ${shipping}`"></td>
                      </tr>

                      <tr>
                        <th>Gesamtpreis</th>
                        <th></th>
                        <th class="text-end">
                          € {{ getTotal }}
                        </th>
                      </tr>
                    </tbody>
                  </v-table>
                </v-sheet>
              </template>
            </v-stepper>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
import ShoppingCart from './ShoppingCart.vue';

export default {
  name: 'checkout',
  components: { 
    ShoppingCart,
  },
  props: [],
  data() {
    return {
      shipping: 10,
      step: 1,
      items: [
          'Bestellung Prüfen',
          'Lieferart auswählen',
          'Bestätigen',
      ],
    };
  },
  methods: {

  },
  mounted() {
  },
  computed: {
    getTotal() {
      // Calculate the total by summing product prices and shipping cost
      const productTotal = this.cart.reduce(
        (acc, product) => acc + product.amount * product.price,
        0
      );
      return productTotal + parseInt(this.shipping);
    },
    cart() {
      return this.$store.state.cart;
    },
  },
}
</script>

<style scoped>
.max-width-card {
}

.checkout {
  /* Add any additional styling for the section if needed */
}
</style>
