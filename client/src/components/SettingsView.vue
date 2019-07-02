<template>
  <div class="db-container">
    <div>
      <div class="data-section">
        <div class="input-header">
          Use status:
          <input
            type="checkbox"
            id="use_status"
            name="use_status"
            :checked="status_checked == true ? true : false"
            @change="$_useStatusChanged()"
            v-model="use_status"
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
            id="use_quarantine"
            name="use_quarantine"
            :checked="quarantine_checked == true ? true : false"
            :disabled="quarantine_disabled == true ? true : false"
            @change="$_useQuarantineChanged()"
            v-model="use_quarantine"
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
          Hours, minutes and seconds (hh:mm:ss) until reserved item is quarantined.
          Only used when quarantine is in use.
        </div>
      </div>
      <button
        type="submit"
        id="save-settings"
        class="btn setting-save"
        @click="$_saveSettings()"
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
  },
  methods: {
    $_useStatusChanged() {
      this.quarantine_disabled = this.use_status == true ? false : true;
      this.use_quarantine = this.use_status == true ? this.use_quarantine : false;
      this.$_useQuarantineChanged()
    },
    $_useQuarantineChanged() {
      this.timeout_disabled = this.use_quarantine == true ? false : true;
      this.timeout = this.use_quarantine == true ? this.timeout : "23:59:59";
    },
    $_saveSettings() {
      axios
        .put("/api/v1/settings", {
          use_status: this.use_status,
          use_quarantine: this.use_quarantine,
          timeout: this.timeout
        })
        .then(response => {
          this.$emit("submit", "ok", "Settings saved");
        })
        .catch(error => {
          var errorData = error["response"]["data"];
          this.$emit(
            "submit",
            "error",
            errorData["title"] + " (" + errorData["detail"] + ")"
          );
        });
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
