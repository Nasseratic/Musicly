<template>
  <div id="app">
    <app-navbar/>
    <div class="container">
      <router-view/>
    </div>
  </div>

</template>

<script>
import AppNavbar from './components/app-nav'
export default {
  name: 'app',
  components: {
    AppNavbar
  }
}
</script>

<style>
@import '../node_modules/bulma/css/bulma.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.card{
  padding: 0px;
}

</style>