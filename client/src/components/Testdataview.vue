<template>
  <div class="content">
    <h3>Datasets</h3>
      <template v-for="dataset in Object.keys(testdata)">
          <span>Dataset: {{ dataset }}</span>
          <div v-for="item in testdata[dataset]">
            <span>Item: {{ item.item }} - Timestamp: {{ item.timestamp }}</span>
          </div>
      </template>
  </div>
</template>

<script>
const axios = require('axios');

export default {
    name: 'Testdataview',
    data() {
        return {
            testdata: [],
            errors: []
        };
    },
    created() {
        axios.get(`/api/v1/testdata`)
            .then(response => (this.testdata = response.data.testdata))
            .catch(error => (this.errors = error))
    }
};
</script>

<style>
   @import '../assets/styles/testdataserver.css';
</style>
