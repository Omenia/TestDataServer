<template>
  <div class="data-section">
    <div class="section-header">Existing datasets</div>
    <div v-for="dataset in testdata" :key="dataset.dataset">
      <div
        class="conf-dataset-row conf-name-icons-row"
        :class="$_datasetTaClass(dataset.dataset, 'name')"
        @click="$_toggleDataset(dataset.dataset)"
      >
        <ul class="left">
          <li class="conf-dataset-name">
            {{ dataset.dataset }}
            <span class="conf-datatype">- {{ dataset.datatype }}</span>
          </li>
        </ul>
        <ul class="right">
          <li
            class="conf-item-modify"
            :class="$_datasetTaClass(dataset.dataset, 'delete')"
            @click="$_confirmDatasetDelete(dataset.dataset)"
            title="Delete dataset"
          >
            <font-awesome-icon size="1x" icon="trash-alt"/>
          </li>
        </ul>
      </div>
      <div
        class="conf-dataset-item-row conf-name-icons-row"
        v-for="(item, index) in dataset.items"
        :key="item.item"
        :style="{ display: openedDatasets[dataset.dataset] }"
      >
        <ul class="left">
          <li
            class="conf-item-name"
            :class="$_itemTaClass(dataset.dataset, index, 'name')"
          >{{ item.item }}</li>
        </ul>
        <ul class="right">
          <li
            v-if="['quarantined', 'out of use'].indexOf(item.status) >= 0"
            class="conf-item-modify"
            :class="$_statusClass(item.status)"
          >
            <div :class="$_itemTaClass(dataset.dataset, index, 'status')">{{ item.status }}</div>
          </li>
          <li
            v-if="['quarantined', 'out of use'].indexOf(item.status) >= 0"
            class="conf-item-modify"
            :class="$_itemTaClass(dataset.dataset, index, 'play')"
            @click="$_updateItemStatus(dataset.dataset, item.item, 'available')"
            title="Take item into use"
          >
            <font-awesome-icon
              size="1x"
              icon="play-circle"
              :class="$_itemTaClass(dataset.dataset, index, 'play-icon')"
            />
          </li>
          <li
            v-else
            class="conf-item-modify"
            :class="$_itemTaClass(dataset.dataset, index, 'stop')"
            @click="$_updateItemStatus(dataset.dataset, item.item, 'out of use')"
            title="Take item out of use"
          >
            <font-awesome-icon
              size="1x"
              icon="stop-circle"
              :class="$_itemTaClass(dataset.dataset, index, 'stop-icon')"
            />
          </li>
          <li
            class="conf-item-modify"
            :class="$_itemTaClass(dataset.dataset, index, 'delete')"
            @click="$_confirmItemDelete(dataset.dataset, item.item)"
            title="Delete dataset item"
          >
            <font-awesome-icon size="1x" icon="trash-alt"/>
          </li>
        </ul>
      </div>
      <div
        :class="['add-item-' + dataset.dataset]"
        class="conf-add-item"
        @click="$_toggleAddItem(dataset.dataset)"
        title="Add new item"
        :style="{ display: openedDatasets[dataset.dataset] }"
      >
        <font-awesome-icon size="1x" icon="plus-square"/>
      </div>
      <span
        class="conf-new-item-container"
        :style="{ display: addItemContainers[dataset.dataset] }"
      >
        <span class="conf-new-item-element" :style="{ display: addItems[dataset.dataset] }">
          <input
            type="text"
            name="new-item"
            id="new-dataset-item"
            placeholder="New item data"
            required
            v-model="newItem"
          >
        </span>
        <button
          type="submit"
          id="submit-new-item"
          class="btn conf-new-item-element"
          @click="$_submitAddItem(dataset.dataset)"
          :style="{ display: addItems[dataset.dataset] }"
        >Submit</button>
      </span>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTrashAlt } from "@fortawesome/free-solid-svg-icons";
import { faPlusSquare } from "@fortawesome/free-solid-svg-icons";
import { faPlayCircle } from "@fortawesome/free-solid-svg-icons";
import { faStopCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faTrashAlt, faPlusSquare, faPlayCircle, faStopCircle);

Vue.component("font-awesome-icon", FontAwesomeIcon);

const axios = require("axios");

export default {
  name: "ExistingDatasets",
  props: {
    testdata: {
      type: String,
      required: true,
    }, 
    openedDatasets: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      testdata: {},
      datatype: "",
      openedDatasets: {},
      addItemContainers: {},
      addItems: {},
      errors: []
    };
  },
  methods: {
    $_toggleDataset: function(dataset) {
      if (this.openedDatasets[dataset] == "flex") {
        this.$set(this.openedDatasets, dataset, "none");
        this.$set(this.addItemContainers, dataset, "none");
      } else {
        this.$set(this.openedDatasets, dataset, "flex");
        this.$set(this.addItemContainers, dataset, "list-item");
      }
    },
    $_confirmDatasetDelete: function(dataset) {
      if (confirm("Are you sure you want to delete dataset: " + dataset)) {
        axios
          .delete("/api/v1/testdata/" + dataset)
          .then(response => {
            this.$emit("submit", "ok", "Dataset deleted");
            axios
              .get(`/api/v1/testdata`)
              .then(response => {
                var testdata = response.data.testdata;
                var openedDatasets = {};
                this.testdata = testdata;
              })
              .catch(error => {
                this.errors = error;
              });
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
    },
    $_confirmItemDelete: function(dataset, item) {
      if (
        confirm(
          "Are you sure you want to delete dataset item: " +
            dataset +
            " - " +
            item
        )
      ) {
        axios
          .delete("/api/v1/testdata/" + dataset + "/" + item)
          .then(response => {
            this.$emit("submit", "ok", "Dataset item deleted");
            axios
              .get(`/api/v1/testdata`)
              .then(response => {
                var testdata = response.data.testdata;
                var openedDatasets = {};
                this.testdata = testdata;
              })
              .catch(error => {
                this.errors = error;
              });
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
    },
    $_datasetTaClass: function(dataset, element) {
      var className = "ta-" + element + "-" + dataset;
      return { [className]: true };
    },
    $_itemTaClass: function(dataset, index, element) {
      var className = "ta-" + element + "-" + dataset + "-" + index;
      return { [className]: true };
    },
    $_toggleAddItem(dataset) {
      if (this.addItems[dataset] == "flex") {
        this.$set(this.addItems, dataset, "none");
      } else {
        this.$set(this.addItems, dataset, "flex");
      }
    },
    $_submitAddItem(dataset) {
      axios
        .post("/api/v1/testdata/" + dataset + "/" + this.newItem, {})
        .then(response => {
          this.$set(this.addItems, dataset, "none");
          this.newItem = "";
          this.$emit("submit", "ok", "Item added");
        })
        .catch(error => {
          var errorData = error["response"]["data"];
          this.$emit(
            "submit",
            "error",
            errorData["title"] + " (" + errorData["detail"] + ")"
          );
        });
    },
    $_updateItemStatus(dataset, item, status) {
      axios
        .put("/api/v1/testdata/" + dataset + "/" + item, { status: status })
        .then(response => {
          var len = this.testdata.length;
          for (var i = 0; i < len; i++) {
            if (this.testdata[i]["dataset"] === dataset) {
              var itemsLen = this.testdata[i]["items"].length;
              for (var j = 0; j < itemsLen; j++) {
                if (this.testdata[i]["items"][j]["item"] === item) {
                  this.testdata[i]["items"][j]["status"] = status;
                  break;
                }
              }
              break;
            }
          }
          this.$emit("submit", "ok", "Item is set " + status);
        })
        .catch(error => {
          var errorData = error["response"]["data"];
          this.$emit(
            "submit",
            "error",
            errorData["title"] + " (" + errorData["detail"] + ")"
          );
        });
    },
    $_statusClass: function(status) {
      var className = "conf-status-" + status.split(" ").join("-");
      return { [className]: true };
    }
  }
};
</script>

<style>
@import "../assets/styles/testdataserver.css";
</style>
