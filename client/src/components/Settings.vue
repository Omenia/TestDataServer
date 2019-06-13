<template>
  <div id="settings">
    <Header/>
    <Navigation/>
    <Testdataview/>
  </div>
</template>

<script>
import Header from './Header';
import Navigation from './Navigation';

export default {
  name: 'Settings',
  components: {
    Header,
    Navigation,
  },
};
</script>

<style>
  @import '../assets/styles/testdataserver.css';
</style> 
