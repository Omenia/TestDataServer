<template>
  <div class="content">
    <h3>Datasets</h3>
    <div v-for="dataset in Object.keys(testdata)" v-bind:key="dataset">
      <span>Dataset: {{ dataset }}</span>
      <div v-for="item in testdata[dataset]" v-bind:key="item.item">
        <span>Item: {{ item.item }} - Timestamp: {{ item.timestamp }}</span>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "Testdataview",
  data() {
    return {
      testdata: [],
      errors: []
    };
  },
  created() {
    axios
      .get(`/api/v1/testdata`)
      .then(response => (this.testdata = response.data.testdata))
      .catch(error => (this.errors = error));
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
