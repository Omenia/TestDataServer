<template>
  <div class="test-data-view">
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
        axios.get(`/testdata/all`)
            .then(response => (this.testdata = response.data.testdata))
            .catch(error => (this.errors = error))
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>