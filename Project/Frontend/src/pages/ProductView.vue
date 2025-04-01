<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<!--author <Sarish-->
<template>
  <v-container class="product-view">
    <v-row align="center">
      <v-col cols="4" class="align-start">
        <v-row>
          <v-skeleton-loader :loading="loading" type="image">
            <product-image
              :product="product"
            />
          </v-skeleton-loader>
        </v-row>
      </v-col>
      <v-col cols="4">
        <v-skeleton-loader :loading="loading" type="article">
          <v-row>
            <span class="product-title">{{ product.name }}</span>
          </v-row>
          <v-row>
            <span class="description">{{ product.desc }}</span>
          </v-row>
          <v-row>
            <v-divider />
          </v-row>
          <v-row>
            <review :productId="$route.params.id" />
          </v-row>
        </v-skeleton-loader>
      </v-col>
      <v-col cols="4">
        <v-container class="cart-box">
          <v-skeleton-loader :loading="loading" type="article">
            <v-container>
              <v-row>
                <span class="product-price">{{ product.price }} €</span>
              </v-row>
              <v-row>
                <span>Lieferung 20€</span>
              </v-row>
              <v-row>{{ product.stock }}</v-row>
              <v-row>
                <v-btn color="primary" @click="addToCart()">In den Einkaufswagen</v-btn>
              </v-row>
              <v-row>
                <v-btn :disabled="true">Jetzt kaufen</v-btn>
              </v-row>
            </v-container>
          </v-skeleton-loader>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Review from '@/components/Review.vue';
import ProductService from '@/Services/ProductService';
import ProductImage from '../components/ProductImage.vue';

export default {
  name: 'product-view',
  components: {
    Review,
    ProductImage,
  },
  props: {},
  async mounted() {
    const id = this.$route.params.id;
    this.loading = true;
    try {
      this.product = await ProductService.get(id);
    } catch (error) {
      console.error(error);
      alert(error);
    }
    this.loading = false;
  },
  data() {
    return {
      loading: false,
      product: {
        "id": 1,
        "name": "Product 1",
        "desc": "Description 1",
        "price": 19.99,
        "stock": 13,
        "imgpath": "path/to/img1"
      },
    }
  },
  methods: {
    addToCart() {
      try {
        this.$store.dispatch('addToCart', this.product);
        alert('Product added to your cart!');
      } catch (error) {
        console.error(error);
        alert("Couldn't add the product to the cart!");
      }
    },
  },
  computed: {},
}
</script>

<style scoped>
.product-title {
  font-size: 24px;
  line-height: 32px;
  text-rendering: optimizeLegibility;
  word-break: break-word;
  box-sizing: border-box;
  font-weight: 400;
  color: #0F1111;
}
.product-price {
  font-size: 28px;
  line-height: normal;
  box-sizing: border-box;
  color: #0F1111;
}

.cart-box {
  border: 1px #d5d9d9 solid;
  border-top: none;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  border-radius: 0 0 8px 8px;
  position: fixed;
  top: 0;
  right: 0;
  margin-top: 55px;
  max-width: 25%;
  display: block;
  box-sizing: border-box;
  font-size: 14px;
}

.description {
  color: #0F1111;
  box-sizing: border-box;
  word-wrap: break-word;
  font-size: 14px;
  line-height: 20px;
}

.image {
  max-height: 442px;
  max-width: 442px;
  height: 100%;
  width: auto;
  vertical-align: top;
  border: 0;
  box-sizing: border-box;
  text-align: center;
}
</style>