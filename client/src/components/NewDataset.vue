<template>
  <div class="form-group">
    <div class="section-header">Add new dataset</div>
    <label for="new-dataset">Dataset name</label>
    <input
      type="text"
      name="dataset"
      id="new-dataset"
      class="form-field ta_new_dataset_name"
      required
      v-model="dataset"
    >
    <label for="new-dataset">Dataset items</label>
    <textarea
      name="items"
      id="new-dataset-items"
      class="form-control ta_new_dataset_items"
      placeholder='One item in a line. Example: 
        {"username": "user1", "password": "passwd", "email": "user1@example.com"}
        {"username": "user2", "password": "passwd", "email": "user2@example.com"}'
      rows="5"
      required
      v-model="items"
    ></textarea>
    <button type="submit" class="btn ta_new_dataset_submit" @click="submitNewDataset">Submit</button>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "NewDataset",
  data() {
    return {
      dataset: "",
      items: "",
    };
  },
  methods: {
    submitNewDataset() {
      var itemList = this.items.split("\n");

      axios
        .post("/api/v1/testdata", {
          dataset: this.dataset,
          items: itemList
        })
        .then(response => {
          this.dataset = "";
          this.items = "";
          this.$emit("submit", "ok", "Dataset added");
        })
        .catch(error => {
          var errorData = error["response"]["data"]
          this.$emit("submit", "error",  errorData["title"] + " (" + errorData["detail"] + ")");
        });
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
