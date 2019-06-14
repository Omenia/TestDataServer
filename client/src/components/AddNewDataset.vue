<template>
  <div class="form-group">
    <div class="section-header ta-add-new-dataset-header" id="add-new-dataset-header" @click="toggle_new_dataset()">Add new dataset</div>
    <div id="add-new-dataset-section" :style="{ display: showAddNew }">
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
</template>

<script>
import Vue from "vue";

const axios = require("axios");

export default {
  name: "AddNewDataset",
  data() {
    return { 
      newDataset: "",
      showAddNew: "none",
      errors: [],
    };
  },
  methods: {
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
        })
        .catch(error => {
          var errorData = error["response"]["data"]
          this.$emit("submit", "error",  errorData["title"] + " (" + errorData["detail"] + ")", null);
        });
    },
  },
};
</script>

<style>
  @import "../assets/styles/testdataserver.css";
</style>
