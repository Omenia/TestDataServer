import Vue from 'vue'
import ConfigurationPage from './components/ConfigurationPage'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { ConfigurationPage },
  template: '<ConfigurationPage/>'
});
