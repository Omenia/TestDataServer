<template>
  <div id="settings">
    <Header/>
    <Navigation/>
    <Testdataview/>
  </div>
</template>

<script>
import Navigation from './Navigation';

export default {
  name: 'Settings',
  components: {
    Navigation,
  },
};
</script>

<style>
  @import '../assets/styles/testdataserver.css';
</style> 
