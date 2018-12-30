<template>
  <div class="content">
    <NewDataset/>
  </div>
</template>

<script>
const axios = require("axios");

import NewDataset from "./NewDataset";

export default {
  name: "Configview",
  components: {
    NewDataset
  },
  data() {
    return {
      testdata: [],
      errors: []
    };
  },
  // todo: take into use when implementing existing dataset view
  // created() {
  //   axios
  //     .get(`/api/v1/testdata`)
  //     .then(response => (this.testdata = response.data.testdata))
  //     .catch(error => (this.errors = error));
  // }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
