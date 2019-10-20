import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Strategy from "../views/Strategy";
import Notice from "../views/Notice";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/strategy',
    name: 'strategy',
    component: Strategy
  },
  {
    path: '/notice',
    name: 'notice',
    component: Notice
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
