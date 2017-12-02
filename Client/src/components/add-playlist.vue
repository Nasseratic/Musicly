<template>
  <div>
    <section class="hero is-small is-primary is-bold">
        <div class="hero-body super">
          <div class="container">
            <h1 class="title">
              ADD PLAYLIST
            </h1>
          </div>
        </div>
    </section>
    <br>
    <form v-on:submit="sub" class="container">
        <div class="field">
          <div class="control">
            <input v-model="name" class="input" type="text" placeholder="Name">
          </div>
        </div>

        <div class="field">
          <div class="control">
            <textarea v-model="description" class="textarea" placeholder="Description"></textarea>
          </div>
        </div>
        <button class="button is-primary is-medium btn-text" type="submit">ADD</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'add-playlist',
  data: () => { return {
      name: "",
      description: "",
  }},
   methods: {
    sub: function(event){
          if(this.name == "" || this.description == ""){
            event.preventDefault();
          }else{
            event.preventDefault();
            let url = 'http://127.0.0.1:8000/music/addPlaylist/';
            let data= { 'name': this.name , 'description': this.description};
            axios.post(url , data).then( (res) => {
              console.log(res.data);
              this.$router.push('/');
            });
        }   
    }
  }
}
</script>
