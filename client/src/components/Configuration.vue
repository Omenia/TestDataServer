<template>
  <div id="configuration" class="container ta_configuration_header">
    <div class="nav">
      <Navigation active_page="configuration"/>
    </div>
    <Configview/>
  </div>
</template>

<script>
import Header from "./Header";
import Navigation from "./Navigation";
import Configview from "./Configview";

export default {
  name: "Configuration",
  components: {
    Header,
    Navigation,
    Configview
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>