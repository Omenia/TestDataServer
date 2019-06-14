import Vue from 'vue'
import Configuration from './components/Configuration'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { Configuration },
  template: '<Configuration/>'
});
