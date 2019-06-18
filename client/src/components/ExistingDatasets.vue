<template>
  <div class="conf-testdata"> 
    <div class="section-header">Existing datasets</div>
    <div v-for="dataset in testdata" :key="dataset.dataset">
      <div class="conf-dataset-row conf-name-icons-row" :class="dataset_ta_class(dataset.dataset, 'name')" @click="toggle_dataset(dataset.dataset)">
        <ul class="left">
          <li class="conf-dataset-name">
            {{ dataset.dataset }} 
            <span class="conf-datatype"> - {{ dataset.datatype }}</span>
          </li>
        </ul>
        <ul class="right">
          <li class="conf-item-modify" :class="dataset_ta_class(dataset.dataset, 'delete')" @click="confirm_dataset_delete(dataset.dataset)" title="Delete dataset">
            <font-awesome-icon size="1x" icon="trash-alt"/>
          </li>
        </ul>
      </div>
      <div class="conf-dataset-item-row conf-name-icons-row" v-for="(item, index) in dataset.items" :key="item.item" :style="{ display: openedDatasets[dataset.dataset] }">
        <ul class="left">
          <li class="conf-item-name" :class="item_ta_class(dataset.dataset, index, 'name')">{{ item.item }}</li>
        </ul>
        <ul class="right">
          <li class="conf-item-modify" :class="item_ta_class(dataset.dataset, index, 'delete')" @click="confirm_item_delete(dataset.dataset, item.item)" title="Delete dataset item">
            <font-awesome-icon size="1x" icon="trash-alt"/>
          </li>
        </ul>
      </div>
      <div :class="['add-item-' + dataset.dataset]" class="conf-add-item" @click="toggle_add_item(dataset.dataset)"  title="Add new item" :style="{ display: openedDatasets[dataset.dataset] }">
        <font-awesome-icon size="1x" icon="plus-square"/>
      </div>
      <span class="conf-new-item-container" :style="{ display: addItemContainers[dataset.dataset] }">
        <span class="conf-new-item-element" :style="{ display: addItems[dataset.dataset] }">
          <input
            type="text"
            name="new-item"
            id="new-dataset-item"
            placeholder="New item data"
            required
            v-model="newItem"
          >
        </span>
        <button type="submit" id="submit-new-item" class="btn new-item-element" @click="submitAddItem(dataset.dataset)" :style="{ display: addItems[dataset.dataset] }">Submit</button>
      </span>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTrashAlt } from "@fortawesome/free-solid-svg-icons";
import { faPlusSquare } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faTrashAlt);
library.add(faPlusSquare);

Vue.component("font-awesome-icon", FontAwesomeIcon);

const axios = require("axios");

export default {
  name: "ExistingDatasets",
  props: ['testdata', 'openedDatasets'],
  data() {
    return { 
      testdata: {},
      items: "",
      datatype: "",
      openedDatasets: {},
      addItemContainers: {},
      addItems: {},
      errors: [],
    };
  },
  methods: {
    toggle_dataset: function(dataset) {
      if (this.openedDatasets[dataset] == "flex") {
        this.$set(this.openedDatasets, dataset, "none");
        this.$set(this.addItemContainers, dataset, "none");
      } else {
        this.$set(this.openedDatasets, dataset, "flex")
        this.$set(this.addItemContainers, dataset, "list-item");
      }
    },
    confirm_dataset_delete: function (dataset) {
      if (confirm("Are you sure you want to delete dataset: " + dataset)) {
        axios
          .delete("/api/v1/testdata/" + dataset)
          .then((response) => {
            this.$emit("submit", "ok", "Dataset deleted");
            axios
              .get(`/api/v1/testdata`)
              .then((response) => {
                var testdata = response.data.testdata;
                var openedDatasets = {};
                this.testdata = testdata;
              })
              .catch(error => {this.errors = error})
        })
        .catch(error => {
          var errorData = error["response"]["data"]
          this.$emit("submit", "error",  errorData["title"] + " (" + errorData["detail"] + ")");          
        });
      }
    },
    confirm_item_delete: function (dataset, item) {
      if (confirm("Are you sure you want to delete dataset item: " + dataset + " - " + item)) {
        axios
          .delete("/api/v1/testdata/" + dataset + "/" + item)
          .then((response) => {
            this.$emit("submit", "ok", "Dataset item deleted");
            axios
              .get(`/api/v1/testdata`)
              .then((response) => {
                var testdata = response.data.testdata;
                var openedDatasets = {};
                this.testdata = testdata;
              })
              .catch(error => {this.errors = error})
        })
        .catch(error => {
          var errorData = error["response"]["data"]
          this.$emit("submit", "error", errorData["title"] + " (" + errorData["detail"] + ")");
        });
      }
    },
    dataset_ta_class: function (dataset, element) {
      var className = "ta-" + element + "-" + dataset;
      return {[className]: true}
    },
    item_ta_class: function (dataset, index, element) {
      var className = "ta-" + element + "-" + dataset + "-" + index;
      return {[className]: true}
    },
    toggle_add_item(dataset) {
      if (this.addItems[dataset] == "flex") {
        this.$set(this.addItems, dataset, "none")
      } else {
        this.$set(this.addItems, dataset, "flex")
      }
    },
    submitAddItem(dataset) {
      axios
        .post( "/api/v1/testdata/" + dataset + "/" + this.newItem, {})
        .then(response => {
          this.$emit("submit", "ok", "Item added");
          axios
              .get(`/api/v1/testdata`)
              .then((response) => {
                var openedDatasets = {};
                this.testdata = response.data.testdata;
                this.$set(this.addItems, dataset, "none");
                this.newItem = "";
              })
              .catch(error => {this.errors = error})
        })
        .catch(error => {
          var errorData = error["response"]["data"]
          this.$emit("submit", "error",  errorData["title"] + " (" + errorData["detail"] + ")");
        });
    },
  },
};
</script>

<style>
  @import "../assets/styles/testdataserver.css";
</style>
