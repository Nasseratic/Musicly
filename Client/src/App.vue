<template>
  <div id="app">
    <app-navbar/>
    
      <router-view/>

  </div>

</template>

<script>
import AppNavbar from './app-nav'
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
  margin: 7px;
}
.card-footer-item{
  height: 100%;
  border-radius: 0px;
}

.columns{
  margin-top: 15px; 
}

</style>