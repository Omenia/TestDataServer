<template>
    <div class="nav">
        <ul id="navigation">
            <li v-for="link in Object.values(links)">
                <a v-bind:class="link.element_class" v-bind:href="link.url" v-bind:title="link.tooltip">
                    <font-awesome-icon size="2x" v-bind:icon="link.icon" />
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTachometerAlt } from '@fortawesome/free-solid-svg-icons'
import { faInfo } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faTachometerAlt, faInfo)

Vue.component('font-awesome-icon', FontAwesomeIcon)

export default {
  name: 'Navigation',
  props: ['active_page'],
  data() {
    return {
        active_link: this.active_page,
        links: {
            dashboard: {
                url: '/',
                icon: 'tachometer-alt',
                tooltip: 'Dashboard',
                element_class: 'deactive_page'
            },
            swagger: {
                url: '/ui',
                icon: 'info',
                tooltip: 'API documentation',
                element_class: 'deactive_page'
            }
        }
    }
  },
  created() {
      this.links[this.active_link]['element_class'] = 'active_page';
  }
};
</script>

<style>
    @import '../assets/styles/testdataserver.css';
</style>
