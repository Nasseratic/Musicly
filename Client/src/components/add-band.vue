<template>
  <div>
    <br><br>
    <form v-on:submit="sub" class="container">
      <div class="columns">
        <div class="column is-7">
          <div class="control">
            <input v-model="name" class="input is-large" type="text" placeholder="Name">
          </div>
        </div>
      </div>
      <button class="button is-primary is-outlined is-large btn-text" type="submit">ADD</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'add-band',
  data(){
    return{ name:'' }
  },
  methods: {
    sub: function(event){
          if(this.name == ""){
            event.preventDefault();
          }else{
            event.preventDefault();
            let url = "http://127.0.0.1:8000/music/addBand/";
            let data = { 'name': this.name };
            axios.post(url , data).then( (res) => {
              console.log(res.data);
              this.$router.push('/artists');
            });
        }   
    }
  }
}
</script>

<style scoped>
.column{
  margin: 0 auto;
}
</style>
