<template>
  <div class="columns">
  <div class="card column is-4">
    <header class="card-header">
      <p class="card-header-title">
        Component
      </p>
      <a href="#" class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fa fa-angle-down" aria-hidden="true"></i>
        </span>
      </a>
    </header>
    <div class="card-content">
      <div class="content">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.
        <a href="#">@bulmaio</a>.
        <a href="#">#css</a>
        <a href="#">#responsive</a>
        <br>
        <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
      </div>
    </div>
    <footer class="card-footer">
      <a href="#" class="card-footer-item button is-primary">   <i class="material-icons">play_arrow</i></a>
      <a href="#" class="card-footer-item button  "> <i class="material-icons">playlist_add</i></a>
    </footer>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'playlists',
    data: () => {
      return { playlists:[] }
    },
    created() {
      let $url = '...';    
      axios.get( $url + '/playlist').then( res =>{
        this.playlist = JSON.parse(res);
      }).catch( err =>{
        console.log(this.albums)
        alert(err);
      });
    }
  }
</script>

<style>
.card-footer-item{
  height: 100%;
  border-radius: 0px;
}

</style>
