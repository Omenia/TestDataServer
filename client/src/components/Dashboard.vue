<template>
  <div id="dashboard" class="container ta_dashboard_header">
    <div class="nav">
      <Navigation active_page="dashboard"/>
    </div>
    <div class="content">
      <div>
        <info-area :class="[infoStyle]">{{ infoMsg }}</info-area>
        <TestdataView/>
      </div>
    </div>
  </div>
</template>

<script>
import Navigation from "./Navigation";
import InfoArea from "./Info";
import TestdataView from "./TestdataView";

export default {
  name: "Dashboard",
  components: {
    Navigation,
    InfoArea,
    TestdataView
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
