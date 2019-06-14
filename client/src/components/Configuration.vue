<template>
  <div id="configuration" class="container ta_configuration_header">
    <div class="nav">
      <Navigation active_page="configuration"/>
    </div>
    <div class="content">
      <div>
        <info-area :class="[infoStyle]"> {{ infoMsg }} </info-area>
        <existing-datasets v-on:submit="update_info" :testdata="testdata" :openedDatasets="openedDatasets"></existing-datasets>
        <add-new-dataset v-on:submit="update_testdata_and_info"></add-new-dataset>
      </div>
    </div>
  </div>
</template>

<script>
import Navigation from "./Navigation";
import InfoArea from "./Info";
import ExistingDatasets from "./ExistingDatasets";
import AddNewDataset from "./AddNewDataset"; 

const axios = require("axios");

export default {
  name: "Configuration",
  components: {
    Navigation,
    InfoArea,
    ExistingDatasets,
    AddNewDataset
  },
  data() {
    return {
      infoMsg: "",
      infoStyle: "hidden-info",
      testdata: {},
      openedDatasets: {},
      errors: [],
    }
  },
  created() {
    axios
      .get(`/api/v1/testdata`)
      .then((response) => {
        var testdata = response.data.testdata;
        var openedDatasets = {};
        for (var dataset in testdata) {
          openedDatasets[dataset] = "none";
        }
        this.testdata = testdata;
        this.openedDatasets = openedDatasets;
      })
      .catch(error => {this.errors = error})
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
    },
    update_testdata_and_info: function(status, msg) {
      this.update_info(status, msg)
      if (status == 'ok') {
        axios
              .get(`/api/v1/testdata`)
              .then((response) => {
                var openedDatasets = {};
                this.testdata = response.data.testdata;
              })
              .catch(error => {this.errors = error})
      }
    }
  }
};

</script>

<style>
  @import "../assets/styles/testdataserver.css";
</style>