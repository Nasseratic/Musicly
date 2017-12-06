<template>
  <div class="app-nav card">
    <nav class="navbar is-transparent">
  <div class="navbar-brand">
    <a class="navbar-item" href="#/">
      <img src="./assets/logo.png" alt="Bulma: a modern CSS framework based on Flexbox">
    </a>
    <div class="navbar-burger burger" data-target="navbarExampleTransparentExample">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>

  <div id="navbarExampleTransparentExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item" href="#/">
        HOME
      </a>
      <a class="navbar-item" href="#/songslist">
        SONGS
      </a>
      <a class="navbar-item" href="#/playlists">
        PLAYLISTS
      </a>
      <a class="navbar-item" href="#/albums">
        ALBUMS
      </a>
      <a class="navbar-item" href="#/artists">
        ARTISTS
      </a>
    </div>

  </div>
</nav>
  </div>
</template>

<script>
export default {
  name: 'app-nav',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card{
  margin: 0px;
}
img{
  max-width: 250px ;
}
.app-nav{
  margin-bottom: 1px;
}
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
