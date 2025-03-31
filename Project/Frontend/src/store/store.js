// edited by Yannic
// edited by Miles Sasportas
// store/index.js
import ProductService from '@/Services/ProductService';
import { createStore } from 'vuex';
//import ProductService from "../Services/ProductService.js";

export default createStore({
  state() {
    return {
      user: null,
      cart: [],
      favorites: [],
    };
  },
  getters: {
    user(state) {
      return state.user;
    },
    cart(state) {
      if (state.cart.length === 0) {
        state.cart = JSON.parse(localStorage.getItem("cart")) || [];
      }

      return state.cart;
    },
    favorites(state) {
      return state.favorites;
    },
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    addToCart(state, product) {
      const existingProduct = state.cart.find(p => p.id === product.id);
      if (existingProduct) {
        existingProduct.amount += 1;
        existingProduct.amount = Math.min(existingProduct.stock, existingProduct.amount);
      } else {
        state.cart.push(Object.assign({ amount: 1 }, product));
      }
    },
    removeFromCart(state, productId) {
      state.cart = state.cart.filter(item => item.id !== productId);
    },
    clearCart(state) {
      state.cart = [];
    },
    saveCart(state) {
      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    async initialiseStore(state) {
      const cart = JSON.parse(localStorage.getItem("cart"));
      state.cart = cart ? cart : [];
      const favorites = await ProductService.getFavoriteProducts();
      state.favorites = favorites;
    },
    toggleFavorite(state, fproduct) {
      const index = state.favorites.findIndex(product => product.id === fproduct.id);
    
      if (index !== -1) {
        // Product is already a favorite, remove it
        state.favorites.splice(index, 1);
      } else {
        // Product is not a favorite, add it
        state.favorites.push(fproduct);
      }
    },
  },
  actions: {
    updateUser({ commit }, user) {
      commit('setUser', user);
    },
    addToCart({ commit }, product) {
      commit('addToCart', product);
      commit('saveCart');
    },
    removeFromCart({ commit }, productId) {
      commit('removeFromCart', productId);
      commit('saveCart');
    },
    clearCart({ commit }) {
      commit('clearCart');
      commit('saveCart');
    },
    toggleFavorite({ commit }, productId) {
      commit('toggleFavorite', productId);
    },
  },
});
