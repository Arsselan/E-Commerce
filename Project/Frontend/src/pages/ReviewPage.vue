<!--author <Sarish,Arsselan-->
<template>
  <div>
    <h2>Product Details</h2>
    <div v-if="product" class="product-details">
      <v-img :src="product.get_image" height="200" class="product-image"></v-img>
      <div class="description">
        <h3>Name: {{ product.name }}</h3>
        <h3>Beschreibung: {{ product.desc }}</h3>
        <h3>Anzahl: {{ product.stock }}</h3>
        <h3>Preis: {{ product.price }}</h3>
      </div>
    </div>
    <div v-else>
      <p>Loading product...</p>
      <p v-if="loadingError">Error loading product details. Please try again later.</p>
    </div>

   
    <div style="height: 30px;"></div>

    <h2>Review Section</h2>
    <Review :reviews="reviews" />
  </div>
</template>

<script>
import Review from "@/components/Review.vue";
import ProductService from "../Services/ProductService";

export default {
  name: 'ProductDetailPage',
  components: {
    Review,
  },
  data() {
    return {
      product: null,
      reviews: [],
      productId: null,
      loadingError: false,
    };
  },
  created() {
    this.productId = this.$route.params.productId;
    this.loadProductDetails();
    this.loadReviews();
  },
  methods: {
    async loadProductDetails() {
      try {
        this.product = await ProductService.getProductById(this.productId);
      } catch (error) {
        console.error('Error loading product details:', error);
        this.loadingError = true;
      }
    },
    async loadReviews() {
      try {
        this.reviews = await ProductService.getReviews(this.productId);
      } catch (error) {
        console.error('Error loading reviews:', error);
      }
    },
    
  },
};
</script>
<!--author <Arsselan-->
<style scoped>
.product-details {
  display: flex;
  align-items: flex-start;
}

.product-image {
  max-width: 150px;
  margin-right: 20px; 
  margin-left: auto;
  margin-top: 20px;
}

.description {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-left: 20px;
  margin-right: auto;
  margin-top: 40px;
}
</style>
