<template>
  <div id="settings" class="container ta_settings_header">
    <div class="nav">
      <Navigation active_page="settings"/>
    </div>
    <div class="content">
      <div>
        <info-area :class="[infoStyle]">{{ infoMsg }}</info-area>
        <SettingsView/>
      </div>
    </div>
  </div>  
</template>

<script>
import Navigation from './Navigation';
import InfoArea from "./Info";
import SettingsView from "./SettingsView";

export default {
  name: "Settings",
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
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>