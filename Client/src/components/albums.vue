<<template>
  <div id='albums'>

  </div>
</template>

<script>
export default {
  name: 'albums',
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
