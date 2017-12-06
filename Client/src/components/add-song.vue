<template>
   <div class="container">
    <br>
    <form v-on:submit="sub" class="container">
      <div class="field">
        <div class="control">
          <input class="input" v-model="name" type="text" placeholder="Name">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="path" type="text" placeholder="Path">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="releaseDate" type="text" placeholder="releaseDate">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="length" type="number" placeholder="length">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="genre" type="text" placeholder="genre">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="artist" type="text" placeholder="artist">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="lyrics" type="text" placeholder="lyrics">
        </div>
      </div>
      <button class="button is-primary is-medium btn-text" type="submit">ADD</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'add-song',
  data(){
    return { name:'' , path:'' , releaseDate: '' , length: 0  , genre:'', artist : '' , lyrics:'Not Avilable' , band : '' , album :''  }
  },
  methods: {
    sub: function(event){
          
            event.preventDefault();
            let url = "http://127.0.0.1:8000/music/addSong/";
            let data = {name:this.name , path:this.path , artist : this.artist, releaseDate: this.releaseDate , length:this.length , genre:this.genre, lyrics:this.lyrics , band : '' , album :'' } ;
            axios.post(url , data).then( (res) => {
              console.log(res.data);
              this.$router.push('/songslist');
            });
          
    }
  }
}
</script>
