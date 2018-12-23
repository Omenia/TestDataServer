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
#settings {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
