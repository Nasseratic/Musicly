<template>
  <div class="songs-list">
  <section class="hero is-medium is-primary is-bold">
  <div class="hero-body super">
    <div class="container">
      <h1 class="title">
        {{$route.params.type}}
      </h1>
    </div>
  </div>
</section>
<div class=" container">
  <div class="card" style="padding:50px; margin-top:-100px;">
      <a-player :music="{
  title: 'Preparation',
  author: 'Hans Zimmer/Richard Harvey',
  url: './src/assets/Naruto 3.mp3',
  pic: './src/assets/bg2.png',
  lrc: '[00:00.00]lrc here\n[00:01.00]aplayer'
  }"></a-player>
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
        songs: []
      }
    },
    components: {
        'a-player': VueAplayer
    },
    created(){
      let url = 'http://127.0.0.1:8000/music/';
      let type = this.$route.params.type;
      let id = this.$route.params.id;
      if( id && type){
          url = url + `${type}/${id}`;
      }else{
        url = url + 'allSongs/';
      }

      axios.get(url).then(res => {
        this.songs = res.data;
      }).catch( err => {
        alert(err);
      });
      
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
            this.songs = res.data;
          }).catch( err => {
            alert(err);
          });
      }
    }

  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

</style>
