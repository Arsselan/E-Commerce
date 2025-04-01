<!--author <Arsselan-->
<template>
  <section class="product-list">
    <v-progress-circular v-if="productsLoading" indeterminate color="primary"></v-progress-circular>
    <v-row v-else>
      <v-col v-for="product in products" :key="product.id" cols="12" md="4">
        <v-card @click="goToReview(product.id)">
          <v-col class="text-right">
            <v-btn icon class="ma-2" @click.stop="toggleFavorite(product)">
              <v-icon :color="isFavorite(product) ? 'red' : ''">mdi-heart</v-icon>
            </v-btn>
          </v-col>
          <v-img :src="product.get_image" height="200"></v-img>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.desc }}</v-card-subtitle>
          <v-card-text>
            Price: ${{ product.price.toFixed(2) }}<br />
            Stock: {{ product.stock }}
          </v-card-text>
          <v-btn block class="mb-8" color="primary" size="large" @click.stop="addToCart(product)">
            In den Einkaufswagen
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </section>
</template>
<!--author <Arsselan-->
<script>
import ProductService from "../Services/ProductService.js";

export default {
  name: 'product-list',
  props: {},
  data() {
    return {
      products: [],
      productsLoading: true,
    };
  },
  methods: {
    async getProducts() {
      try {
        this.products = await ProductService.getFavoriteProducts(this.search);
      } catch (error) {
        console.error(error);
        alert(error);
      }
      this.productsLoading = false;
    },
    goToReview(productId) {
      this.$router.push(`/product/${productId}`);
    },
    addToCart(product) {
      // Add the product to the cart
      this.$store.dispatch('addToCart', product);
    },
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
    isFavorite(fproduct) {
      return this.$store.getters.favorites.some(product => product.id === fproduct.id);
    },
  },
  computed: {
    search() {
      return this.$route.query.query;
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
