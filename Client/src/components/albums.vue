<<template>
  <div id='albums'>
    <section class="hero is-bold is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            ALBUMS
          </h1>
        </div>
      </div>
    </section>
    <div class="container">
    <div class="columns">
      <div class="card column is-4" v-for="album in albums">
        <header class="card-header">
          <p class="card-header-title">
            {{album.title}}
          </p>
          <a v-on:click="del(album.id)" class="card-header-icon" aria-label="more options">
            <span class="icon">
             <i class="material-icons">delete</i>
            </span>
          </a>
        </header>
        <div class="card-content">
          <div class="content">
            BAND : <a href="#"> #{{album.band}} </a>
            <br>
          </div>
        </div>
        <footer class="card-footer">
          <a href="#" class="card-footer-item button is-primary">
            <i class="material-icons">play_arrow</i>
          </a>
        </footer>
      </div>
    </div>
    </div>
    <router-link to="../add/album">
       <fab></fab>
      </router-link>
  </div>
  </template>

  <script>
    import axios from "axios";
    import fab from 'vue-fab'
    
    export default {
      components:{
        fab
      },
      name: 'albums',
      data: () => {
        return {
          albums: []
        }
      },
      created() {
        let $url = 'http://127.0.0.1:8000/music/allAlbums/';
        axios.get($url).then(res => {
          this.albums = JSON.parse(res.data).map( e => { e.fields['id'] = e.pk; return e.fields });
        }).catch(err => {
          alert(err);
        });
      },
      methods:{
      del(id){
        let $url = 'http://127.0.0.1:8000/music/delAlbum/'+id;
        axios.get($url).then(res => {
          this.albums = JSON.parse(res.data).map( e => { e.fields['id'] = e.pk ;  return e.fields } );
        }).catch(err => {
          alert(err);
        });  
      }
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
  </style>
