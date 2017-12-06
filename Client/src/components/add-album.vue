<template>
   <div class="container">
    <br>
    <form v-on:submit="sub" class="container">
      <div class="field">
        <div class="control">
          <input class="input" v-model="title" type="text" placeholder="Title">
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input class="input" v-model="band" type="text" placeholder="Band">
        </div>
      </div>
      <button class="button is-primary is-medium btn-text" type="submit">ADD</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'add-album',
  data(){
    return { title:'' , band : 3  }
  },
  methods: {
    sub: function(event){
          if(this.title == "" || this.band == ""){
            event.preventDefault();
          }else{
            event.preventDefault();
            let url = "http://127.0.0.1:8000/music/addAlbum/";
            let data = { 'title': this.title , 'band':this.band};
            axios.post(url , data).then( (res) => {
              console.log(res.data);
              this.$router.push('/albums');
            });
        }   
    }
  }
}
</script>
