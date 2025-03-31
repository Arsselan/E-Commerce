// edited by Yannic
// edited by Miles Sasportas
import { ApiService } from "./ApiService";

class ProductService extends ApiService {
    constructor() {
        super();
    }
    //author: Arsselan
    async getProductById(productId) {
        try {
          const response = await this.axios.get(`product/${productId}`);
          return response.data; 
        } catch (error) {
          console.error('Error fetching product details:', error);
          throw error;
        }
    }
    async getAll(search) {
        if (this.isDevelopment) {
            let products =  [{ 
                "id": 1,
                 "name": "Product 1!", 
                 "desc": "Description 1", 
                 "price": 19.99, 
                 "stock": 10, 
                 "imgpath": "path/to/img1"
                }, { 
                    "id": 2, "name": "Product 2!", "desc": "Description 2", "price": 99.99, "stock": 20, "imgpath": "path/to/img2" }, { "id": 3, "name": "Product 3", "desc": "Description 3", "price": 57.99, "stock": 15, "imgpath": "path/to/img3" }, { "id": 4, "name": "Product 4", "desc": "Description 4", "price": 280.0, "stock": 5, "imgpath": "path/to/img4" }, { "id": 5, "name": "Product 5", "desc": "Description 5", "price": 77.77, "stock": 12, "imgpath": "path/to/img5" }, { "id": 6, "name": "Product 6", "desc": "Description 6", "price": 333.33, "stock": 8, "imgpath": "path/to/img6" }
            ];

            if (search) {
                products = products.filter(p => p.name.includes(search))
            }

            return products;
        }

        const response = !search
            ? await this.axios.get("product/")
            : await this.axios.get("search/", {
                params: {
                    q: search,
                }
            })
        return response.data;
    }

    async getBySeller() {
        const response = await this.axios.get("product/seller/")
        return response.data;
    }

    async addToCart (id) {
          const response = await this.axios.post("addToCart/", {
            id: id,
          });
          return response.data;
      }

      async get(id) {
        if (this.isDevelopment) {
            return {
                "id": 1,
                 "name": "Product 1", 
                 "desc": "Description 1", 
                 "price": 19.99, 
                 "stock": 10, 
                 "imgpath": "path/to/img1"
            };
        }

        if (id instanceof Number) {
            throw "Expected a number!";
        }
        
        const response = await this.axios.get(`product/${id}`);
        return response.data;
    }
    //author: Sarish

    async getReviews(productId) {
        const response = await this.axios.get(`product/${productId}/review/`);
        return response.data;
    }
    //author: Sarish

    async addReview(productId, reviewData) {
        const response = await this.axios.post(`product/${productId}/review/`, reviewData);
        return response.data;
    }
    //author: Sarish

    async deleteReview(reviewId) {
        const response = await this.axios.delete(`product/delete_review/${reviewId}/`)
        return response.data;
    }

    async uploadProduct(formData) {
        try {
            const response = await this.axios.post('seller/upload_product/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            return response.data;
        } catch (error) {
            console.error('Error uploading product:', error);
            throw error;
        }
    }
    //author: Sarish
    async getFavoriteProducts() {
        try {
            const response = await this.axios.get('product/list_favorite/');
            const favoriteData = response.data;

            // Extract product IDs from the favorite data
            const productIds = favoriteData.map(item => item.productid);

            // Fetch product details for each product ID
            const favoriteProducts = await Promise.all(
                productIds.map(productId => this.getProductById(productId))
            );

            return favoriteProducts;
        } catch (error) {
            console.error('Error fetching favorite products:', error);
            return [];
        }
    }
    //author: Arsselan
    async addFavorite(productId) {
        const response = await this.axios.post(`product/add_favorite/${productId}/`);
        return response.data;
    }
    //author: Arsselan
    async deleteFavorite(favoriteId){
        const response = await this.axios.delete(`product/delete_favorite/${favoriteId}/`)
        return response.data;
    }

    async updateProduct(product) {
        try {
            const response = await this.axios.put(`seller/update_product/${product.id}`, product);
            return response.data;
        } catch (error) {
            console.error('Error updating product:', error);
            throw error;
        }
    }
    async deleteProduct(product) {
        try {
            const response = await this.axios.delete(`seller/delete_product/${product.id}`);
            return response.data;
        } catch (error) {
            console.error('Error deleting product:', error);
            throw error;
        }
    }
}

export default new ProductService();
