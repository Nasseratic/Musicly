<template>
  <div class="songs-list">
    <transition name="list">
      <div class="modal" v-bind:class="{ 'is-active': isActive }">
        <div class="modal-background" @click="modtoggle"></div>
        <div class="modal-content">
          <form v-on:submit="sub">
            <div>
              <div class="control">
                <input v-model="playlistId" class="input is-large" type="text" placeholder="playlist id">
              </div>
            </div>
            <br>
            <button class="button is-primary is-outlined is-large btn-text" type="submit">ADD</button>
          </form>
        </div>
        <button class="modal-close is-large" aria-label="close" @click="modtoggle"></button>
      </div>
    </transition>
    <section class="hero is-medium is-primary is-bold">
      <div class="hero-body super">
        <div class="container">
          <h1 class="title">
            <span v-if="$route.params.type">{{$route.params.type}} : </span> {{name}}
          </h1>
        </div>
      </div>
    </section>
    <div class=" container">
      <div class="card main-card" style="padding:50px; margin-top:-100px;">
        <transition-group name="list">
          <div class="card" v-for="(song , index) in songs" v-bind:key="song.name">
            <a-player :music="{
            title: song.name,
            author: (artists[index] ? artists[index].name : 'unkown'),
            url: './src/assets'+ (song.path[0]=='/' ? song.path : '/'+ song.path) ,
            pic: './src/assets/bg2.png',
            lrc: song.lyrics
            }"></a-player>
            <footer v-if="!$route.params.type" class="card-footer">
              <a class="card-footer-item button is-primary is-outlined " disabled>
                Lyrics : {{song.lyrics}}
                <i class="material-icons">error</i>
              </a>
              <a v-on:click="addToPlaylist(song.id)" class="card-footer-item button is-link is-outlined">
                Add To Play List
                <i class="material-icons">playlist_add</i>
              </a>
              <a v-on:click="del(song.id)" class="card-footer-item button is-outlined is-danger">
                Delete
                <i class="material-icons">delete</i>
              </a>

            </footer>
          </div>
        </transition-group>
      </div>
    </div>
    <router-link to="../add/song">

      <fab></fab>
    </router-link>
  </div>
</template>

<script>
import VueAplayer from "vue-aplayer";
import axios from "axios";
import fab from "vue-fab";

export default {
  name: "songs-list",
  data() {
    return {
      isActive: false,
      name: "ALL",
      songs: [],
      artists: [],
      songId: "",
      playlistId: ""
    };
  },
  components: {
    "a-player": VueAplayer,
    fab: fab
  },
  created() {
    let url = "http://127.0.0.1:8000/music/";
    let type = this.$route.params.type;
    let id = this.$route.params.id;
    if (id && type && (type == "playlist") | (type == "album")) {
      url = url + `${type}/${id}`;
      axios
        .get(url)
        .then(res => {
          this.songs = JSON.parse(res.data.songs).map(e => {
            e.fields["id"] = e.pk;
            return e.fields;
          });
          this.artists = JSON.parse(res.data.artists).map(e => {
            return e.fields;
          });
          if (type == "playlist") {
            this.name = JSON.parse(res.data.type)[0].fields.name;
          } else {
            this.name = JSON.parse(res.data.type)[0].fields.title;
          }
        })
        .catch(err => {
          alert(err);
        });
    } else {
      url = url + "allSongs/";
      axios
        .get(url)
        .then(res => {
          this.songs = JSON.parse(res.data).map(e => {
            e.fields["id"] = e.pk;
            return e.fields;
          });
        })
        .catch(err => {
          alert(err);
        });
    }
  },
  watch: {
    $route(to, from) {
      let url = "http://127.0.0.1:8000/music/";
      let type = this.$route.params.type;
      let id = this.$route.params.id;
      if (id && type && (type == "playlist") | (type == "album")) {
        url = url + `${type}/${id}`;
        axios
          .get(url)
          .then(res => {
            this.songs = JSON.parse(res.data.songs).map(e => {
              e.fields["id"] = e.pk;
              return e.fields;
            });
            this.artists = JSON.parse(res.data.artists).map(e => {
              return e.fields;
            });
            if (type == "playlist") {
              this.name = JSON.parse(res.data.type)[0].fields.name;
            } else {
              this.name = JSON.parse(res.data.type)[0].fields.title;
            }
          })
          .catch(err => {
            alert(err);
          });
      } else {
        url = url + "allSongs/";
        axios
          .get(url)
          .then(res => {
            this.songs = JSON.parse(res.data).map(e => {
              e.fields["id"] = e.pk;
              return e.fields;
            });
          })
          .catch(err => {
            alert(err);
          });
      }
    }
  },
  methods: {
    modtoggle() {
      this.isActive = !this.isActive;
    },
    addToPlaylist(id) {
      this.modtoggle();
      this.songId = id;
    },
    sub() {
      if ((this.songId == "") | (this.playlistId == "")) {
        event.preventDefault();
      } else {
        event.preventDefault();
        let url = `http://127.0.0.1:8000/music/addSongToPlaylist/${this
          .songId}/${this.playlistId}`;
        axios.get(url).then(res => {
          this.$router.push("/playlists");
        });
      }
    },
    del(id) {
      let $url = "http://127.0.0.1:8000/music/delSong/" + id;
      axios
        .get($url)
        .then(res => {
          this.songs = JSON.parse(res.data).map(e => {
            e.fields["id"] = e.pk;
            return e.fields;
          });
        })
        .catch(err => {
          alert(err);
        });
    }
  }
};
</script>

<style scoped>
.card-footer {
  margin-top: 20px;
}
.card {
  padding: 15px;
}
.main-card {
  min-height: 50vh;
}
.is-lite {
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
.title {
  font-size: 3.4em;
  margin-top: -50px;
  text-transform: uppercase;
}
.subtitle {
  font-size: 1.5em;
}

.list-enter-active,
.list-leave-active {
  transition: all 2s;
}
.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(60px);
}
</style>
