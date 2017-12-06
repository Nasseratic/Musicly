<template>
  <transition name="fade">
    
  <div v-if="show">
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
            <div class="column is-one-third" v-for="playlist in playlists" v-bind:key="playlist.id">
              <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  #{{playlist.id}} {{playlist.name}}
                </p>
                <a v-on:click="del(playlist.id)" class="card-header-icon" aria-label="more options">
                  <span class="icon">
                     <i class="material-icons">delete</i>
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
                <a v-on:click="goToList(playlist.id)" class="card-footer-item button is-primary">
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
      <router-link to="../add/playlist">
       <fab></fab>
      </router-link>
    </div>
  </transition>
</template>

<script>
  import axios from "axios";
  import fab from 'vue-fab'

  export default {
    name: 'playlists',
    components: {
      fab
    },
    data: () => {
      return {
        playlists: [],
        show:false
      }
    },
    created() {
      
      setTimeout(() => {
      let $url = 'http://127.0.0.1:8000/music/allPlaylists/';
      axios.get($url).then(res => {
        this.playlists= JSON.parse(res.data).map( item => { item.fields['id'] = item.pk; return item.fields } );
      }).catch(err => {
        alert(err);
      });
      this.show = true;
      }, 600);
    },
    methods :{
      del(id){
        let $url = 'http://127.0.0.1:8000/music/delPlaylist/'+id;
        axios.get($url).then( res => {
          this.playlists= JSON.parse(res.data).map( item => { item.fields['id'] = item.pk; return item.fields } );
        });
      },
      goToList(id){
        this.$router.push('../songslist/playlist/'+id);
      },
    }
  }

</script>

<style scoped>
.icon{
  color: firebrick;
}
.icon :hover{
  color: red;
}
.list-enter-active, .list-leave-active {
  transition: all 3s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(50px);
}
.fade-enter-active  {
  transition: opacity .7s
}
.fade-leave-active{
  transition: opacity .7s  
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

</style>
