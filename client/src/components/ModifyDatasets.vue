<template>
  <div class="config-testdata"> 
    <div class="section-header">Existing datasets</div>
    <div v-for="dataset in Object.keys(testdata)" v-bind:key="dataset">
      <div class="dataset-row">
        <span class="dataset-name" :class="dataset_ta_class(dataset, 'name')" @click="toggle(dataset)">{{ dataset }}</span> 
        <span class="item-modify" :class="dataset_ta_class(dataset, 'delete')" @click="confirm_dataset_delete(dataset)" title="Delete dataset"><font-awesome-icon size="1x" icon="trash-alt"/></span>
      </div>
      <div class="dataset-item-row" v-for="(item, index) in testdata[dataset]" v-bind:key="item.item" v-bind:style="{ display: openedDatasets[dataset] }">
        <span class="item-name" :class="item_ta_class(dataset, index, 'name')">{{ item.item }}</span>
        <span class="item-modify" :class="item_ta_class(dataset, index, 'delete')" @click="confirm_item_delete(dataset, item.item)" title="Delete dataset item"><font-awesome-icon size="1x" icon="trash-alt"/></span>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTrashAlt } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faTrashAlt);

Vue.component("font-awesome-icon", FontAwesomeIcon);

const axios = require("axios");

export default {
  name: "ModifyDatasets",
  data() {
    return { 
      testdata: {},
      openedDatasets: {},
      // dataset: "",
      // items: "",
      errors: [],
    };
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
    toggle: function(dataset) {
      if (this.openedDatasets[dataset] == "none") {
        this.$set(this.openedDatasets, dataset, "inherit")
      } else {
        this.$set(this.openedDatasets, dataset, "none")
      }
    },
    confirm_dataset_delete: function (dataset) {
      if (confirm("Are you sure you want to delete dataset: " + dataset)) {
        axios
          .delete("/api/v1/testdata/" + dataset)
          .then((response) => {
          })
          .catch(error => {this.errors = error})
      }
    },
    confirm_item_delete: function (dataset, item) {
      if (confirm("Are you sure you want to delete dataset item: " + dataset + " - " + item)) {
        axios
          .delete("/api/v1/testdata/" + dataset + "/" + item)
          .then((response) => {
          })
          .catch(error => {this.errors = error})
      }
    },
    dataset_ta_class: function (dataset, element) {
      var className = "ta_" + element + "_" + dataset;
      return {[className]: true}
    },
    item_ta_class: function (dataset, index, element) {
      var className = "ta_" + element + "_" + dataset + "_" + index;
      return {[className]: true}
    }
  }    
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
