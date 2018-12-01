import Vue from 'vue'
import Router from 'vue-router'


const routerOption = [
  { path: '/', name:'home', component: 'Home' },
  { path: '/graph', name:'graph', component: 'Graph' },
  { path: '/search/:key?', name:'search', component: 'Search' },
  { path: '/about', name:'about', component: 'About' },
  { path: '/wiki/:key', name:'wiki', component: 'Wiki' },
  { path: '*', name:'404' ,component: 'NotFound' },
]

const routes = routerOption.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})