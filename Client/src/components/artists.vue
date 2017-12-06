<template>
<transition name="fade">
  <div id="artists" v-show="show">
    <section class="hero is-bold is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            ARTISTS
          </h1>
        </div>
      </div>
    </section>
    <div class="container">
      <transition-group name="list" class="columns is-multiline">
        <div class="column is-4" v-for="artist in artists" v-bind:key="artist.id">
          <div class="card ">
                
              <article class="media">
                <div class="media-left">
                  <figure class="image is-64x64">
                    <img src="src/assets/bg.png" alt="Image">
                  </figure>
                </div>
                <div class="media-content">
                  <div class="content">
                    <p>
                      <strong>{{artist.name}}</strong>
                      <br>
                      <small>{{artist.dateOfBirth}}</small>
                      <br>
                      <strong v-if="artist.band">@{{artist.band}}</strong>
                    </p>
                  </div>
                </div>
              </article>
              <a v-on:click="del(artist.id)" class=" is-small button is-outlined is-danger">
                 Delete <i class="material-icons">delete</i>
              </a>
          </div>
        </div>
      </transition-group>
    </div>
      <router-link to="../add/artist">
       <fab></fab>
      </router-link>
  </div>
</transition>
</template>

<script>
  import axios from 'axios'
  import fab from 'vue-fab'
  export default {
    components:{
      fab
    },
    name: 'artists',
    data: () => {
      return {
        artists: [],
        show:false
      }
    },
    created() {
      setTimeout(() => {
        this.show = true
        let $url = 'http://127.0.0.1:8000/music/allArtist';
        axios.get($url).then(res => {
          this.artists = JSON.parse(res.data).map( e => { e.fields['id'] = e.pk ;  return e.fields } );
        }).catch(err => {
          alert(err);
        });  
      }, 600);
    
    },
    methods:{
      del(id){
        let $url = 'http://127.0.0.1:8000/music/delArtist/'+id;
        axios.get($url).then(res => {
          this.artists = JSON.parse(res.data).map( e => { e.fields['id'] = e.pk ;  return e.fields } );
        }).catch(err => {
          alert(err);
        });  
      }
    }

  }

</script>

<style scoped>
  .card {
    padding: 30px;
  }

.list-enter-active, .list-leave-active {
  transition: all 2s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(-30px);
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
