<template>
  <div id="configuration">
    <Header/>
    <Navigation/>
  </div>
</template>

<script>
import Header from './Header';
import Navigation from './Navigation';

export default {
  name: 'Configuration',
  components: {
    Header,
    Navigation,
  },
};
</script>

<style>
#configuration {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
