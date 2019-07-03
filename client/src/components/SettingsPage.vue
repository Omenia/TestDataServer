<template>
  <div id="settings" class="container ta-settings-header">
    <div class="nav">
      <Navigation active-page="settings"/>
    </div>
    <div class="content">
      <div>
        <info-area :class="[infoStyle]">{{ infoMsg }}</info-area>
        <SettingsView @submit="$_updateInfo"></SettingsView>
      </div>
    </div>
  </div>  
</template>

<script>
import Navigation from './TheNavigation';
import InfoArea from "./TheInfo";
import SettingsView from "./SettingsView";

export default {
  name: "SettingsPage",
  components: {
    Navigation,
    InfoArea,
    SettingsView
  },
  data() {
    return {
      infoMsg: "",
      infoStyle: "hidden-info"
    };
  },
  methods: {
    $_updateInfo: function(status, msg) {
      this.infoMsg = msg;
      if (status == "error") {
        this.infoStyle = "error-info";
      } else {
        this.infoStyle = "ok-info";
        setTimeout(() => {
          this.infoMsg = "";
          this.infoStyle = "hidden-info";
        }, 5000);
      }
    },
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>