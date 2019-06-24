<template>
  <div class="db-container">
    <div>
      <div class="data-section">
        <div class="input-header">
          Use status:
          <input
            type="checkbox"
            id="status_use"
            name="use_status"
            :checked="status_checked == true ? true : false"
          >
        </div>
        <div class="input-description">
          Is item statuses in use?
          <br>If yes, then only available items are returned.
        </div>
      </div>
      <div class="data-section">
        <div class="input-header">
          Use quarantine:
          <input
            type="checkbox"
            id="quarantine_use"
            name="use_quarantine"
            :checked="quarantine_checked == true ? true : false"
            :disabled="quarantine_disabled == true ? true : false"
          >
        </div>
        <div class="input-description">
          Is item quarantine in use?
          <br>If yes, then item which is not released before reservation timeout expires will be quarantined.
          <br>Can only be used when statuses are in use.
        </div>
      </div>
      <div class="data-section">
        <div class="input-header">Reserved item timeout:</div>
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
      status_checked: false,
      use_quarantine: false,
      quarantine_checked: false,
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
        this.status_checked = this.use_status == true ? true : false;
        this.quarantine_checked = this.use_quarantine == true ? true : false;
        this.quarantine_disabled = this.use_status == true ? false : true;
        this.timeout_disabled = this.use_quarantine == true ? false : true;
      })
      .catch(error => (this.errors = error));
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
