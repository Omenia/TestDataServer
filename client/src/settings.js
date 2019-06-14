import Vue from 'vue'
import Settings from './components/Settings'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { Settings },
  template: '<Settings/>'
});
