<template>
  <div class="home">
    <section class="hero is-medium is-primary is-bold">
      <div class="hero-body super">
        <div class="container">
          <h1 class="title">
            WELOCME TO MUSICLY
          </h1>
          <h2 class="subtitle">
            Feel the music
          </h2>
        </div>
      </div>
    </section>
    <section class="hero is-lite">
      <div class="hero-body" style="background: #f9faf9bb;">
        <div class="container">
          <h2 class="subtitle" style="font-weight: 600">
            TOP SONGS
          </h2>
          <div class="card" style="padding:30px;">
            <a-player :music="{
            title: 'Man of the world',
            author: 'Naruto',
            url: './src/assets/Naruto 6.mp3',
            pic: './src/assets/bg2.png',
            lrc: '[00:00.00]lrc here\n[00:01.00]aplayer'
            }"></a-player>

            <a-player :music="{
            title: 'Sadness and Sorrow',
            author: 'Naruto',
            url: './src/assets/Naruto 4.mp3',
            pic: './src/assets/bg2.png',
            lrc: '[00:00.00]lrc here\n[00:01.00]aplayer'
            }"></a-player>
            <br>
            <router-link to="./songslist"> <button class="button is-primary is-medium btn-text"> View ALL Songs </button> </router-link>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
  import VueAplayer from 'vue-aplayer'

  export default {
    name: 'home',
    data() {
      return {

      }
    },
    components: {
      'a-player': VueAplayer
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .is-lite {
    background: #fefefe;
  }

  .super {
    background: url('/src/assets/hero.png');
    background-size: cover;
    background-position: center;
  }

  .title {
    font-weight: 800;
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
  }

  .subtitle {
    font-size: 1.5em;
  }
  .btn-text{
    text-transform: uppercase;
    font-weight: 100;
  }
</style>
