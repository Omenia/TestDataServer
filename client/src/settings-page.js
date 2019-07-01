import Vue from 'vue'
import SettingsPage from './components/settings-page'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  components: { SettingsPage },
  template: '<SettingsPage/>'
});
