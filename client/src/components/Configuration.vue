<template>
  <div id="configuration" class="container ta_configuration_header">
    <div class="nav">
      <Navigation active_page="configuration"/>
    </div>
    <div class="main">
      <Header title="Configuration"></Header>
      <div class="content">
        <ModifyDatasets/>
        <NewDataset/>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "./Header";
import Navigation from "./Navigation";
import ModifyDatasets from "./ModifyDatasets";
import NewDataset from "./NewDataset";

export default {
  name: "Configuration",
  components: {
    Header,
    Navigation,
    ModifyDatasets,
    NewDataset
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>