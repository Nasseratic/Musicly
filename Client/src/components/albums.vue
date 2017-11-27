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
            {{album.name}}
          </p>
          <a href="#" class="card-header-icon" aria-label="more options">
            <span class="icon">
              <i class="fa fa-angle-down" aria-hidden="true"></i>
            </span>
          </a>
        </header>
        <div class="card-content">
          <div class="content">
            <a href="#">@bulmaio</a>.
            <a href="#">#css</a>
            <a href="#">#responsive</a>
            <br>
            <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
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
      name: 'albums',
      data: () => {
        return {
          albums: []
        }
      },
      created() {
        let $url = 'localhost/api/allAlbums';
        axios.get($url).then(res => {
          this.albums = res.data;
        }).catch(err => {
          alert(err);
        });
      }
    }

  </script>

  <style scoped>
   
  </style>
