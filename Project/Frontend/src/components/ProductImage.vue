<!-- edited by Miles Sasportas-->
<template>
  <div v-if="product">
    <v-img
      :src="productImage"
      alt="Product Image"
      :height="height"
    />
  </div>
</template>

<script>
export default {
  name: 'product-image',
  props: {
    product: {
      // type: Object,
      // required: true,
    },
    height: {
      type: Number,
      required: false,
      default: 200,
    }
  },
  data() {
    return {
    };
  },
  computed: {
    productImage() {
      return this.product.get_image && this.product.get_image != "https://localhost:8000/media/default_image.png" 
        ? this.product.get_image
        : `https://robohash.org/${this.product.id}?set=set1&size=200x200`;
    },
  },
};
</script>

<style scoped>
</style>
