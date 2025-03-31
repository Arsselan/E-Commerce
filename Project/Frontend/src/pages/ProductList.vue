<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<!--author <Sarish-->
<!--co-author <Arsselan-->
<template>
  <section class="product-list">
    <v-progress-circular v-if="productsLoading" indeterminate color="primary"></v-progress-circular>
    <v-row v-else>
      <v-col v-for="product in products" :key="product.id" cols="12" md="4">
        <v-card @click="goToReview(product.id)">
          <v-col class="text-right">
            <v-btn
              v-if="account"
              icon
              class="ma-2"
              @click.stop="toggleFavorite(product)"
            >
               <v-icon :color="isFavorite(product) ? 'red' : ''">mdi-heart</v-icon>
            </v-btn>
          </v-col>
          <product-image
            :product="product"
            :height="200"
          />
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.desc }}</v-card-subtitle>
          <v-card-text>
            Preis: €{{ product.price.toFixed(2) }}<br />
            Auf Lager: {{ product.stock }}
          </v-card-text>
          <v-btn block :loading="productsWorking" class="mb-8" color="primary" size="large" @click.stop="addToCart(product)">
            In den Einkaufswagen
          </v-btn>
          <div v-if="isMyProduct(product)">
            <router-link :to="`/edit-product/${product.id}`">
            <v-btn block :loading="productsWorking" class="mb-8" color="light-green" size="large">
              Bearbeiten
            </v-btn>
          </router-link>
            <v-spacer>
            </v-spacer>
            <v-btn block :loading="productsWorking" class="mb-8" color="red" size="large" @click.stop="loeschen(product)">
              Löschen
            </v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import ProductImage from '../components/ProductImage.vue';
import ProductService from "../Services/ProductService.js";

export default {
    components: { ProductImage },
  name: 'product-list',
  props: {},
  data() {
    return {
      products: [],
      productsLoading: true,
      productsWorking: false,

    };
    
  },
  methods: {
    //author: Arsselan
    async getProducts() {
      try {
        if(this.seller) {
          this.products = await ProductService.getBySeller();
        }
        else {
          this.products = await ProductService.getAll(this.search);
        }
      } catch (error) {
        console.error(error);
        alert(error);
      }
      this.productsLoading = false;
    },
    //author: Arsselan
    goToReview(productId) {
      this.$router.push(`/product/${productId}`);
    },
    addToCart(product) {
      // Add the product to the cart
      this.$store.dispatch('addToCart', product);
    },
    //author: Sarish, Arsselan
    async toggleFavorite(product) {
      try {
        if (this.isFavorite(product)) {
          // If already a favorite, remove it
          await ProductService.deleteFavorite(product.id);
        } else {
          // If not a favorite, add it
          await ProductService.addFavorite(product.id);
        }
        // Toggle the favorite status in the Vuex store
        this.$store.dispatch('toggleFavorite', product);
      } catch (error) {
        console.error(error);
        alert(error);
      }
    },
    //author: Sarish

    isFavorite(fproduct) {
      return this.$store.getters.favorites.some(product => product.id === fproduct.id);
    },
    isMyProduct(){
      if (!this.account || !this.account.is_seller) {
        return false;
      }
    //ToDo User and seller ID
      return true
    },
    async loeschen (product){
      if (!confirm("Wirklich loeschen?")){
        return;
      }
      this.productsWorking = true;

      try{
        await ProductService.deleteProduct(product);
        await this.getProducts();
      }
      catch {
        console.log("lol");
      }
      this.productsWorking = false;
    }

  },
  computed: {
    search() {
      return this.$route.query.query;
    },
    seller() {
      return this.$route.query.seller;
    },
    account() {
      return this.$store.getters.user;
    },
  },
  async mounted() {
    await this.getProducts();
  },
  watch: {
    async $route() {
      await this.getProducts();
    },
  },
};
</script>

<style scoped>
.product-list {
  /* Füge hier deine Styles hinzu, wenn nötig */
}
</style>
