<template>
<div id="artists">
 
</div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'artists',
  data: () => {
     return { albums : [] }
  },
  created() {
    let $url = '...';    
    axios.get( $url + '/artists').then( res =>{
      this.artists = JSON.parse(res);
    }).catch( err =>{
      console.log(this.albums)
      alert(err);
    });
  }

}
</script>
