<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<template>
  <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="50%"
      rounded="lg"
  >
    <v-card-title>
      Produkt Hinzufügen
    </v-card-title>
    <v-col cols="12">
      <v-row>
        <v-text-field
          density="compact"
          label="Name"
          variant="outlined"
          v-model="productName"
        ></v-text-field>
      </v-row>
      <v-row>
        <v-textarea
          density="compact"
          label="Description"
          variant="outlined"
          v-model="productDescription"
        ></v-textarea>
      </v-row>
      <v-row>
        <v-col cols="6" style="display: flex;">
          <span class="euro">
            €
          </span>
          <v-text-field
            class="numba"
            density="compact"
            label="Price"
            variant="outlined"
            v-model.number="productPrice"
          ></v-text-field>
        </v-col>
        <v-col cols="6">
          <v-text-field
            class="numba"
            density="compact"
            label="Stock"
            variant="outlined"
            v-model.number="productStock"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-file-input
          v-model="productImage"
          label="Product Image"
          density="compact"
          variant="outlined"
        >
        </v-file-input>
      </v-row>
    </v-col>

    <v-btn
      block
      class="mb-8"
      color="primary"
      size="large"
      :disabled="!productName || !productDescription || !productPrice || !productStock"
      @click="uploadProduct"
      :loading="loading"
    >
      {{ isNew? 'Hochladen' : 'Ändern' }}
    </v-btn>
  </v-card>
</template>


<script>
import ProductService from '../Services/ProductService';

export default {
  props: {
  },
  data() {
    return {
      productName: '',
      productDescription: '',
      productPrice: null,
      productStock: null,
      productImage: [],
      loading: false,
      productLoading: false,
    };
  },
  methods: {
    async uploadProduct() {
      try {
        this.loading = true;
        let product = null;

        if(this.isNew) {
          const formData = new FormData();

          formData.append('name', this.productName);
          formData.append('desc', this.productDescription);
          formData.append('price', this.productPrice);
          formData.append('stock', this.productStock);
          if (this.productImage.length > 0) {
            formData.append('image', this.productImage[0]);
          }
        
          product = await ProductService.uploadProduct(formData);
        }
        else {
          product = await ProductService.updateProduct({
            id: this.productId,
            name: this.productName,
            desc: this.productDescription,
            price: this.productPrice,
            stock: this.productStock,
          });
        }

        this.$router.push(`/product/${product.id}`);
      } catch (error) {
        console.error('Error uploading product:', error);
        alert("Produkt hochladen fehleschlagen")
      }
      this.loading = false;
    },
    async initialize() {
      if (!this.productId) {
        // we want to create new one
        return;
      }

      this.productLoading = true;
      const product = await ProductService.get(this.productId);
      this.productName = product.name;
      this.productDescription = product.desc;
      this.productPrice = product.price;
      this.productStock = product.stock;
      // todo check image
      this.productImage = [];      

      this.productLoading = false;
    },
  },
  computed:{
    isNew() {
      return !this.productId;
    },
    productId() {
      return this.$route.params.productId;
    }
  },
  async mounted() {
    await this.initialize();
  },
};
</script>

<style scoped>
.numba{
  max-width: 400px;
}
.euro{
  font-size: 27px;
  margin-right: 5px;
}
</style>
