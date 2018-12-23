import Vue from 'vue'
import Settings from './components/Settings'
import  Navigation from './components/Navigation'
import  Header from './components/Header'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { Header, Settings },
  template: '<Settings/>'
});
