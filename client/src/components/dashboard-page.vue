<template>
  <div id="dashboard" class="container ta-dashboard-header">
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
  name: "DashboardPage",
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

<style module>
@import "../assets/styles/testdataserver.css";
</style>
