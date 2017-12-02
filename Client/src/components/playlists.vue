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
      <div >
        <transition-group name="list" class="columns is-multiline">
            <div class="column is-one-third" v-for="playlist in playlists" v-bind:key="playlist.name">
              <div class="card">
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
                 PLAY <i class="material-icons">play_arrow</i>
                </a>
                <!-- <a href="#" class="card-footer-item button  ">
                  <i class="material-icons">playlist_add</i>
                </a> -->
              </footer>
              </div>
            </div>
        </transition-group>
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
      let $url = 'http://127.0.0.1:8000/music/allPlaylists/';
      axios.get($url).then(res => {
        this.playlists= JSON.parse(res.data).map( item => { return item.fields } );
      }).catch(err => {
        alert(err);
      });
    }
  }

</script>

<style scoped>

.list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}

</style>
