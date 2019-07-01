<template>
  <ul id="navigation">
    <li v-for="link in Object.values(links)" :key="link.url">
      <a :class="[link.element_class, link.ta_class]" :href="link.url" v-bind:title="link.tooltip">
        <font-awesome-icon size="2x" :icon="link.icon"/>
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
import { faCog } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faTachometerAlt, faDatabase, faInfo, faCog);

Vue.component("font-awesome-icon", FontAwesomeIcon);

export default {
  name: "Navigation",
  props: {
    active_page: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      active_link: this.active_page,
      links: {
        dashboard: {
          url: "/",
          icon: "tachometer-alt",
          tooltip: "Dashboard",
          element_class: "deactive-page",
          ta_class: "ta-dashboard-nav-item"
        },
        configuration: {
          url: "/configuration",
          icon: "database",
          tooltip: "Configuration",
          element_class: "deactive-page",
          ta_class: "ta-configuration-nav-item"
        },
        settings: {
          url: "/settings",
          icon: "cog",
          tooltip: "Settings",
          element_class: "deactive-page",
          ta_class: "ta-settings-nav-item"
        },
        swagger: {
          url: "/ui",
          icon: "info",
          tooltip: "API documentation",
          element_class: "deactive-page",
          ta_class: "ta-swagger-nav-item"
        }
      }
    };
  },
  created() {
    this.links[this.active_link]["element_class"] = "active_page";
  }
};
</script>

<style module>
@import "../assets/styles/testdataserver.css";
</style>
