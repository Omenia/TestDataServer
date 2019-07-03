<template>
  <div id="configuration" class="container ta-configuration-header">
    <div class="nav">
      <Navigation active-page="configuration"/>
    </div>
    <div class="content">
      <div>
        <info-area :class="[infoStyle]">{{ infoMsg }}</info-area>
        <existing-datasets
          v-on:submit="$_updateTestdataAndInfo"
          :testdata="testdata"
          :opened-datasets="openedDatasets"
        ></existing-datasets>
        <add-new-dataset v-on:submit="$_updateTestdataAndInfo"></add-new-dataset>
      </div>
    </div>
  </div>
</template>

<script>
import Navigation from "./TheNavigation";
import InfoArea from "./TheInfo";
import ExistingDatasets from "./ConfigurationDatasetsExisting";
import AddNewDataset from "./ConfigurationDatasetAdd";

const axios = require("axios");

export default {
  name: "ConfigurationPage",
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
      errors: []
    };
  },
  created() {
    axios
      .get(`/api/v1/testdata`)
      .then(response => {
        var testdata = response.data.testdata;
        var openedDatasets = {};
        for (var dataset in testdata) {
          openedDatasets[dataset] = "none";
        }
        this.testdata = testdata;
        this.openedDatasets = openedDatasets;
      })
      .catch(error => {
        this.errors = error;
      });
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
    $_updateTestdataAndInfo: function(status, msg) {
      this.$_updateInfo(status, msg);
      if (status == "ok") {
        axios
          .get(`/api/v1/testdata`)
          .then(response => {
            var openedDatasets = {};
            this.testdata = response.data.testdata;
          })
          .catch(error => {
            this.errors = error;
          });
      }
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>