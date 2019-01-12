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
        "username": "user1", "password": "passwd", "email": "user1@example.com"
        "username": "user2", "password": "passwd", "email": "user2@example.com"'
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
      errors: []
    };
  },
  methods: {
    submitNewDataset() {
      // var itemJson = {};
      var itemList = this.items.split("\n");
      // for (var i = 0; i < itemList.length; i++) {
        // itemJson[i] = itemList[i];
      // }

      axios
        .post("/api/v1/testdata", {
          dataset: this.dataset,
          items: itemList
        })
        .then(response => {
          this.dataset = "";
          this.items = "";
          // todo: take into use when implementing existing dataset view
          // this.$emit("created");
        })
        .catch(error => (this.errors = error));
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
