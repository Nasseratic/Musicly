<template>
  <div id="artists">
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
      <div class="columns">
        <div class="card column is-4" v-for="artist in artists">
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
                  <strong>@{{artist.band}}</strong>
                </p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
  import axios from 'axios'

  export default {
    name: 'artists',
    data: () => {
      return {
        artists: []
      }
    },
    created() {
      let $url = 'localhost:8000/api/allArtist';
      axios.get($url).then(res => {
        this.artists = res.data
      }).catch(err => {
        alert(err);
      });
    }

  }

</script>

<style scoped>
  .card {
    padding: 30px;
  }

</style>
