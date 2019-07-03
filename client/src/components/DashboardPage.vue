<template>
  <div id="dashboard" class="container ta-dashboard-header">
    <div class="nav">
      <Navigation activePage="dashboard"/>
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
import Navigation from "./TheNavigation";
import InfoArea from "./TheInfo";
import TestdataView from "./DashboardTestdataView";

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

<style>
@import "../assets/styles/testdataserver.css";
</style>
