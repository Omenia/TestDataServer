<template>
  <div id="dashboard" class="container">
    <Header title="Dashboard"></Header>
    <div class="main">
      <Navigation active_page="dashboard"/>
      <Testdataview/>
    </div>
  </div>
</template>

<script>
import Header from './Header';
import Navigation from './Navigation';
import Testdataview from './Testdataview';

export default {
  name: 'Dashboard',
  components: {
    Header,
    Navigation,
    Testdataview
  }
};
</script>

<style>
   @import '../assets/styles/testdataserver.css';
</style>
