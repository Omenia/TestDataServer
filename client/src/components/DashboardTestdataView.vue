<template>
  <div class="db-container">
    <div>
      <div class="data-section" v-for="dataset in testdata" :key="dataset.dataset">
        <div class="db-dataset">{{ dataset.dataset }} - {{ dataset.datatype }}</div>
        <div class="db-items" v-for="item in dataset.items" :key="item.item">
          <span class="db-item-row db-item-name">{{ item.item }}</span>
          <span class="db-item-row db-item-time">{{ item.timestamp }}</span>
          <span
            class="db-item-row db-item-status"
            :class="$_statusClass(item.status)"
          >{{ item.status }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "TestdataView",
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
    $_statusClass: function(status) {
      var className = "db-status-" + status.split(" ").join("-");
      return { [className]: true };
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
