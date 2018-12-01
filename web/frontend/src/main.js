import Vue from 'vue'
import App from './App'
import router from './router'
import AtComponents from 'at-ui'
import AtUI from 'at-ui'
import 'at-ui-style'
import global_ from './components/tools/Global'

Vue.use(AtComponents)
Vue.use(AtUI)

Vue.config.productionTip = false

Vue.prototype.GLOBAL = global_

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
