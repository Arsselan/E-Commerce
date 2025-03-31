<!-- edited by Miles Sasportas-->
<!--author <Sarish, Arsselan-->
<template>
  <v-container>
    <v-card-title>Product Reviews</v-card-title>
    <v-list>
      <v-list-item v-if="reviewsComputed.length === 0" :key="0">
        Ouhh this seems pretty empty. There are no reviews available for this product.
      </v-list-item>
    </v-list>

    <v-container v-for="review in reviewsComputed" :key="review.id">
      <v-row>
        <v-rating readonly :length="5" :size="32" v-model="review.rating" active-color="primary" />
      </v-row>
      <v-row>
        <div class="user-comment">{{ review.content }}</div>
      </v-row>
      <v-row>
        <v-list-item-subtitle>
          Created at: {{ review.creationdate }}
        </v-list-item-subtitle>
      </v-row>
      <v-row>
        <v-btn :disabled="user == null || review.userid != user.id" @click="removeReview(review.id)" size="x-small" style="margin-top: 5px; margin-bottom: 10px;">
          Remove
        </v-btn>
      </v-row>
    </v-container>

    <div v-if="user">
      <v-card-title>Add Review</v-card-title>
      <v-row>
        <v-rating hover :length="5" :size="32" v-model="newReview.rating" active-color="primary" />
      </v-row>
      <v-row>
        <v-textarea v-model="newReview.content" label="Comment" variant="outlined"></v-textarea>
      </v-row>
      <v-btn :loading="reviewPosting" @click="submitReview" :disabled="newReview.content.trim() === ''">
        Submit Review
      </v-btn>
    </div>
  </v-container>
</template>

<script>
import ProductService from "../Services/ProductService.js";

export default {
  name: 'Review',
  props: {
    productId: [Number, String],
  },
  data() {
    return {
      newReview: {
        creationdate: "",
        rating: 5,
        content: '',
        product_id: 0,
        userid: 0,
      },
      reviews: [],
      reviewPosting: false,
    };
  },
  async mounted() {
    try {
      this.reviews = await ProductService.getReviews(this.productId);
    } catch (error) {
      console.error('Error loading reviews:', error);
    }
  },
  methods: {
    //author: Sarish
    //co-author: Arsselan
    async submitReview() {
      this.reviewPosting = true;
      try {
        this.newReview.product_id = this.productId;
        this.newReview.creationdate = this.getCurrentDate();
        const response = await ProductService.addReview(this.productId, this.newReview);
        this.newReview.id = response.id;
        this.newReview.userid = response.userid;
        this.reviews.push(this.newReview);
      } catch (error) {
        console.error(error);
        alert("Couldn't post review!");
      } finally {
        this.reviewPosting = false;
        this.newReview = {
          rating: 5,
          content: ''
        };
      }
    },
    //author: Sarish
    async removeReview(id) {
      try {
        await ProductService.deleteReview(id);
        this.reviews = this.reviews.filter(r => r.id != id);
      } catch (error) {
        console.error(error);
        alert("Couldn't delete review!");
      }
    },
    //author: Sarish
    getCurrentDate() {
      const currentDate = new Date();
      const year = currentDate.getFullYear();
      const month = ('0' + (currentDate.getMonth() + 1)).slice(-2);
      const day = ('0' + currentDate.getDate()).slice(-2);
      const formattedDate = year + '-' + month + '-' + day;
      return formattedDate;
    }
  },
  computed: {
    reviewsComputed() {
      return this.reviews;
    },
    user() {
      return this.$store.getters.user;
    }
  }
};
</script>

<style scoped>
.text-center {
  text-align: center;
}
.mb-4 {
  margin-bottom: 1rem;
}
.user-comment {
  white-space: pre-line;
  overflow-wrap: break-word;
  word-wrap: break-word;
  max-width: 80ch;
}
</style>