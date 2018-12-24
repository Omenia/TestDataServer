<template>
  <div id="dashboard" class="container">
    <div class="nav">
      <Navigation active_page="dashboard"/>
    </div>
    <div class="main">
      <Header title="Dashboard"></Header>
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
