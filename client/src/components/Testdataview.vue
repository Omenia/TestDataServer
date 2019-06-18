<template>
  <div class="content">
    <div>
        <h3>Datasets</h3>
        <div class="dashboard-dataset-container" v-for="dataset in testdata" :key="dataset.dataset">
          <div class="dashboard-dataset">{{ dataset.dataset }} - {{ dataset.datatype }}</div>
          <div class="dashboard-items" v-for="item in dataset.items" :key="item.item">
              <span class="dashboard-item-row item-name">{{ item.item }}</span>
              <span class="dashboard-item-row item-time">{{ item.timestamp }}</span>
              <span class="dashboard-item-row item-status" :class="status_class(item.status)">{{ item.status }}</span>
          </div>
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
  },
  methods: {
    status_class: function (status) {
      var className = "status-" + status.split(' ').join('-');
      return {[className]: true}
    }
  }
};
</script>

<style>
  @import "../assets/styles/testdataserver.css";
</style>
