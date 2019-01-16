<template>
  <div id="configuration" class="container ta_configuration_header">
    <div class="nav">
      <Navigation active_page="configuration"/>
    </div>
    <div class="content">
      <div>
        <info-area v-bind:class="[infoStyle]" > {{ infoMsg }} </info-area>
        <modify-datasets v-on:submit="update_info"></modify-datasets>
        <new-dataset v-on:submit="update_info"></new-dataset>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "./Header";
import Navigation from "./Navigation";
import InfoArea from "./Info";
import ModifyDatasets from "./ModifyDatasets";
import NewDataset from "./NewDataset";

export default {
  name: "Configuration",
  components: {
    Header,
    Navigation,
    InfoArea,
    ModifyDatasets,
    NewDataset
  },
  data() {
    return {
      infoMsg: "",
      infoStyle: "hidden-info",
    }
  },
  methods: {
    update_info: function (status, msg) {
      this.infoMsg = msg;
      if (status == "error") {
        this.infoStyle = "error-info";
      }
      else {
        this.infoStyle = "ok-info";
        setTimeout(() => {
          this.infoMsg = "";
          this.infoStyle = "hidden-info"
        }, 5000)
      }
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>