<template>
  <div>
    <div class="config-testdata"> 
      <div class="section-header">Existing datasets</div>
      <div v-for="dataset in testdata" v-bind:key="dataset.dataset">
        <div class="dataset-row">
          <span class="dataset-name" :class="dataset_ta_class(dataset.dataset, 'name')" @click="toggle_dataset(dataset.dataset)">
            {{ dataset.dataset }} 
            <span class="datatype"> - {{ dataset.datatype }}</span>
          </span>
          <span class="item-modify" :class="dataset_ta_class(dataset.dataset, 'delete')" @click="confirm_dataset_delete(dataset.dataset)" title="Delete dataset">
            <font-awesome-icon size="1x" icon="trash-alt"/>
          </span>
        </div>
        <div class="dataset-item-row" v-for="(item, index) in dataset.items" v-bind:key="item.item" v-bind:style="{ display: openedDatasets[dataset.dataset] }">
          <span class="item-name" :class="item_ta_class(dataset.dataset, index, 'name')">{{ item.item }}</span>
          <span class="item-modify" :class="item_ta_class(dataset.dataset, index, 'delete')" @click="confirm_item_delete(dataset.dataset, item.item)" title="Delete dataset item">
            <font-awesome-icon size="1x" icon="trash-alt"/>
          </span>
        </div>
      </div>
    </div>
    <div class="form-group">
      <div class="section-header ta-add-new-dataset-header" id="add-new-dataset-header" @click="toggle_new_dataset()">Add new dataset</div>
      <div id="add-new-dataset-section" v-bind:style="{ display: showAddNew }">
        <label for="new-dataset">Dataset name</label>
        <input
          type="text"
          name="new-dataset"
          id="new-dataset"
          class="form-field ta-new-dataset-name"
          required
          v-model="newDataset"
        >
        <label for="new-dataset">Dataset type</label><br/>
        <select v-model="datatype" name="new-dataset-datatype">
          <option disabled value="">Please select one</option>
          <option value="next">Next</option>
          <option value="random">Random</option>
        </select><br/>
        <label for="new-dataset">Dataset items</label>
        <textarea
          name="items"
          id="new-dataset-items"
          class="form-control ta-new-dataset-items"
          placeholder='One item in a line. Example: 
            {"username": "user1", "password": "passwd", "email": "user1@example.com"}
            {"username": "user2", "password": "passwd", "email": "user2@example.com"}'
          rows="5"
          required
          v-model="items"
        ></textarea>
        <button type="submit" class="btn ta-new-dataset-submit" @click="submitNewDataset">Submit</button>
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
      newDataset: "",
      items: "",
      datatype: "",
      openedDatasets: {},
      showAddNew: "none",
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
    toggle_dataset: function(dataset) {
      if (this.openedDatasets[dataset] == "inherit") {
        this.$set(this.openedDatasets, dataset, "none")
      } else {
        this.$set(this.openedDatasets, dataset, "inherit")
      }
    },
    toggle_new_dataset: function() {
      if (this.showAddNew == "inherit") {
        this.showAddNew = 'none';
      }
      else {
        this.showAddNew = 'inherit';
      }
    },
    submitNewDataset() {
      var itemList = this.items.split("\n");

      axios
        .post("/api/v1/testdata", {
          dataset: this.newDataset,
          items: itemList,
          datatype: this.datatype
        })
        .then(response => {
          this.newDataset = "";
          this.items = "";
          this.$emit("submit", "ok", "Dataset added");
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
      var className = "ta_" + element + "_" + dataset;
      return {[className]: true}
    },
    item_ta_class: function (dataset, index, element) {
      var className = "ta_" + element + "_" + dataset + "_" + index;
      return {[className]: true}
    },
  },
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
