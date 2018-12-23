import Vue from 'vue'
import Configuration from './components/Configuration'
import  Navigation from './components/Navigation'
import  Header from './components/Header'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { Header, Configuration },
  template: '<Configuration/>'
});
