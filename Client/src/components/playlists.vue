<template>
  <div>
      <section class="hero is-bold is-primary">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              PLAYLISTS
            </h1>
          </div>
        </div>
      </section>
      <div class="container">
      <div class="columns">
        <div class="card column is-4" v-for="playlist in playlists">
          <header class="card-header">
            <p class="card-header-title">
              {{playlist.name}}
            </p>
            <a href="#" class="card-header-icon" aria-label="more options">
              <span class="icon">
                <i class="fa fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>
          <div class="card-content">
            <div class="content">
              {{playlist.description}}
            </div>
          </div>
          <footer class="card-footer">
            <a href="#" class="card-footer-item button is-primary">
              <i class="material-icons">play_arrow</i>
            </a>
            <a href="#" class="card-footer-item button  ">
              <i class="material-icons">playlist_add</i>
            </a>
          </footer>
        </div>
      </div>
      </div>
    </div>

</template>

<script>
  import axios from "axios";

  export default {
    name: 'playlists',
    data: () => {
      return {
        playlists: []
      }
    },
    created() {
      let $url = './src/assets/data.json';
      axios.get($url).then(res => {
        this.playlists = res.data;
      }).catch(err => {
        alert(err);
      });
    }
  }

</script>

<style>


</style>
