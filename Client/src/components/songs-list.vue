<template>
  <div class="songs-list">
  <section class="hero is-medium is-primary is-bold">
  <div class="hero-body super">
    <div class="container">
      <h1 class="title">
       <span v-if="$route.params.type">{{$route.params.type}} : </span>  {{name}}
      </h1>
    </div>
  </div>
</section>
<div class=" container">
  <div class="card main-card" style="padding:50px; margin-top:-100px;">
      <transition-group name="list">
          <div class="card" v-for="(song , index) in songs" v-bind:key="song.name" >
          <a-player :music="{
          title: song.name,
          author: (artists[index] ? artists[index].name : 'unkown'),
          url: './src/assets/Naruto 4.mp3',
          pic: './src/assets/bg2.png',
          lrc: song.lyrics
          }"></a-player>
              <footer v-if="!$route.params.type" class="card-footer">
                <a v-on:click="goToList(playlist.id)" class="card-footer-item button is-primary is-outlined " disabled>
                  Lyrics : {{song.lyrics}} <i class="material-icons">error</i>
                </a>
                <a v-on:click="goToList(playlist.id)" class="card-footer-item button is-link is-outlined">
                 Add To Play List  <i class="material-icons">playlist_add</i>
                </a>
                <a v-on:click="goToList(playlist.id)" class="card-footer-item button is-outlined is-danger">
                 Delete <i class="material-icons">delete</i>
                </a>
                <!-- <a href="#" class="card-footer-item button  ">
                  <i class="material-icons">playlist_add</i>
                </a> -->
              </footer>
          </div>
      </transition-group>
  </div>
  </div>
    </div>
  
  </div>
</template>

<script>
  import VueAplayer from 'vue-aplayer'
  import axios from 'axios'
  export default {
    name: 'songs-list',
    data() {
      return {
        name : 'ALL',
        songs: [],
        artists: []
      }
    },
    components: {
        'a-player': VueAplayer
    },
    created(){
      let url = 'http://127.0.0.1:8000/music/';
      let type = this.$route.params.type;
      let id = this.$route.params.id;
      if( id && type && ( type == 'playlist' | type == 'album')  ){
          url = url + `${type}/${id}`;
          axios.get(url).then(res => {
                this.songs =  JSON.parse(res.data.songs).map( e=> { return e.fields } );
                  this.artists = JSON.parse(res.data.artists).map( e=> { return e.fields } );   
                if(type == 'playlist'){
                  this.name =  JSON.parse(res.data.type)[0].fields.name;
                }else{
                  this.name =  JSON.parse(res.data.type)[0].fields.title;              
                }        
            }).catch( err => {
              alert(err);
            });
      }else{
        url = url + 'allSongs/';
        axios.get(url).then(res => {
          this.songs =  JSON.parse(res.data).map( e=> { return e.fields } );          
        }).catch( err => {
              alert(err);
            });
              
      }

      
    },
    watch: {
      '$route' (to, from) {
          let url = 'localhost:8080/api/';
          let type = to.params.type;
          let id =   to.params.id;
          if( id && type){
              url = `${type}/${id}`;
          }

          axios.get(url).then(res => {
            this.songs =  JSON.parse(res.data.songs).map( e=> { return e.fields } );
          }).catch( err => {
            alert(err);
          });
      }
    }

  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-footer{
  margin-top: 20px;
}
  .card{
    padding: 15px;
  }
  .main-card{
    min-height: 50vh;
  }
  .is-lite{
    background: #fefefe;
  }
  h1,
  h2 {
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
  .title{
    font-size: 3.4em;
    margin-top: -50px;
    text-transform: uppercase;
  }
  .subtitle{
    font-size: 1.5em;
  }

  .list-enter-active, .list-leave-active {
  transition: all 2s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(60px);
}

</style>
