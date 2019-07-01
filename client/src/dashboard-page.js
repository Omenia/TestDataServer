import Vue from 'vue'
import DashboardPage from './components/dashboard-page'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { DashboardPage },
  template: '<DashboardPage/>'
});
