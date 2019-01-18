<template>
  <div id="dashboard" class="container ta_dashboard_header">
    <div class="nav">
      <Navigation active_page="dashboard"/>
    </div>
    <Testdataview/>
  </div>
</template>

<script>
import Header from "./Header";
import Navigation from "./Navigation";
import Testdataview from "./Testdataview";

export default {
  name: "Dashboard",
  components: {
    Header,
    Navigation,
    Testdataview
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
