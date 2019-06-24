<template>
  <div class="db-container">
    <div>
      <div class="data-section">
        <div class="input-header">Reserved item timeout</div>
        <div class="settings-timeout-input">
          <input
            type="text"
            name="timeout"
            id="timeout"
            placeholder="hours:minutes:seconds"
            required
            v-model="timeout"
            :disabled="timeout_disabled == true ? true : false"
          >
        </div>
        <div class="input-description">
          Hours, minutes and seconds until reserved item is quarantined.
          Only used when quarantine is in use.
        </div>
      </div>
      <button
        type="submit"
        id="save-settings"
        class="btn setting-save"
        @click="save_settings(dataset.dataset)"
      >Save</button>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "SettingsView",
  data() {
    return {
      use_status: false,
      use_quarantine: false,
      timeout: "00:00:00",
      timeout_disabled: true,
      errors: []
    };
  },
  created() {
    axios
      .get(`/api/v1/settings`)
      .then(response => {
        this.use_status = response.data.settings["use_status"];
        this.use_quarantine = response.data.settings["use_quarantine"];
        this.timeout = response.data.settings["timeout"];
        this.timeout_disabled = this.use_quarantine == true ? false : true;
      })
      .catch(error => (this.errors = error));
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
