import Vue from 'vue'
import DashboardPage from './components/DashboardPage'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { DashboardPage },
  template: '<DashboardPage/>'
});
