import Vue from 'vue'
import Dashboard from './components/Dashboard'
import Navigation from './components/Navigation'
import Header from './components/Header'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { Header, Dashboard },
  template: '<Dashboard/>'
});
