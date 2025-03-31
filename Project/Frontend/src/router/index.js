// edited by Yannic
// edited by Miles Sasportas
import { createRouter, createWebHistory } from 'vue-router'

import PageNotFound from "../pages/PageNotFound";
import Checkout from "../pages/Checkout";
import ProductList from "../pages/ProductList";
import ProductView from "../pages/ProductView";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Overview from "../pages/Overview";
import Review from "../pages/ReviewPage"
import Upload from "../pages/Upload"
import Favorite from "../components/Favorite"

const routes = [
  {
    path: '/:query?:seller?',
    name: 'Home',
    component: ProductList,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: Checkout
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: ProductView
  },
  {
    path: "/:catchAll(.*)",
    name: 'NotFound',
    component: PageNotFound,
  },
  {
    path: "/register",
    name: 'Register',
    component: Register,
  },
  {
    path: "/upload",
    name: 'Upload Product',
    component: Upload,
  },
  {
    path: "/edit-product/:productId",
    name: 'Edit Product',
    component: Upload,
  },
  {
    path: "/account",
    name: 'Account Overview',
    component: Overview,
  },
//author: Sarish

  {
    path: "/DetailReview/:productId",
    name: 'Review',
    component: Review,
  },
//author: Arsselan
  {
    path: "/favorite",
    name: 'Favorite',
    component: Favorite,
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router;

export {
  router,
  routes,
}
