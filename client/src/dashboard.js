import Vue from 'vue'
import Dashboard from './components/Dashboard'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { Dashboard },
  template: '<Dashboard/>'
});
