<template>
  <div id="dashboard">
    <Header title="Dashboard"></Header>
    <Navigation/>
    <Testdataview/>
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
#dashboard {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
