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
          <input class="input" v-model="dateOfBirth" type="text" placeholder="Date Of Birth">
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
  name: 'add-artist',
  data(){
    return{
      name:'',
      dateOfBirth:'',
      band:''
    }
  },
  methods: {
    sub: function(event){
          if(this.name == "" || this.dateOfBirth == ""){
            event.preventDefault();
          }else{
            event.preventDefault();
            let url = "http://127.0.0.1:8000/music/addArtist/";
            let data = { 'name': this.name , 'dateOfBirth': this.dateOfBirth , 'band':this.band};
            axios.post(url , data).then( (res) => {
              console.log(res.data);
              this.$router.push('/artists');
            });
        }   
    }
  }
}
</script>
