<template>
  <ul id="navigation">
    <li v-for="link in Object.values(links)" :key="link.url">
      <a v-bind:class="[link.element_class, link.ta_class]" v-bind:href="link.url" v-bind:title="link.tooltip">
        <font-awesome-icon size="2x" v-bind:icon="link.icon"/>
      </a>
    </li>
  </ul>
</template>

<script>
import Vue from "vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTachometerAlt } from "@fortawesome/free-solid-svg-icons";
import { faDatabase } from "@fortawesome/free-solid-svg-icons";
import { faInfo } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faTachometerAlt, faDatabase, faInfo);

Vue.component("font-awesome-icon", FontAwesomeIcon);

export default {
  name: "Navigation",
  props: ["active_page"],
  data() {
    return {
      active_link: this.active_page,
      links: {
        dashboard: {
          url: "/",
          icon: "tachometer-alt",
          tooltip: "Dashboard",
          element_class: "deactive_page",
          ta_class: "ta_dashboard_nav_item"
        },
        configuration: {
          url: "/configuration",
          icon: "database",
          tooltip: "Configuration",
          element_class: "deactive_page",
          ta_class: "ta_configuration_nav_item"
        },
        swagger: {
          url: "/ui",
          icon: "info",
          tooltip: "API documentation",
          element_class: "deactive_page",
          ta_class: "ta_swagger_nav_item"
        }
      }
    };
  },
  created() {
    this.links[this.active_link]["element_class"] = "active_page";
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
