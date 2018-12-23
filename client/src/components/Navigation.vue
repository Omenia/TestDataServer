<template>
    <ul>
        <li><font-awesome-icon size="2x" icon="tachometer-alt" /></li>
        <li><font-awesome-icon size="2x" icon="info" /></li>
    </ul>

</template>

<script>
import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTachometerAlt } from '@fortawesome/free-solid-svg-icons'
import { faInfo } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faTachometerAlt, faInfo)

Vue.component('font-awesome-icon', FontAwesomeIcon)

export default {
  name: 'Navigation',
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
