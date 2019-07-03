import Vue from 'vue'
import SettingsPage from './components/SettingsPage'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { SettingsPage },
  template: '<SettingsPage/>'
});
