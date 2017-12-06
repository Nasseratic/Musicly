import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home'
import Playlists from '@/components/playlists'
import Artists from '@/components/artists'
import Albums from '@/components/albums'
import AddAlbums from '@/components/add-album'
import AddPlaylist from '@/components/add-playlist'
import AddArtist from '@/components/add-artist'
import AddBand from '@/components/add-band'
import AddSong from '@/components/add-song'
import SongsList from '@/components/songs-list'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/playlists',
      name: 'playlists',
      component: Playlists
    },
    {
      path: '/artists',
      name: 'artists',
      component: Artists
    },
    {
      path: '/albums',
      name: 'albums',
      component: Albums
    },
    {
      path: '/add/song',
      name: 'add-song',
      component: AddSong
    },
    {
      path: '/add/album',
      name: 'add-albums',
      component: AddAlbums
    },
    {
      path: '/add/playlist',
      name: 'add-playlist',
      component: AddPlaylist
    },
    {
      path: '/add/band',
      name: 'add-band',
      component: AddBand
    },
    {
      path: '/add/artist',
      name: 'add-artist',
      component: AddArtist
    },
    {
      path: '/songslist',
      name: 'songslist',
      component: SongsList
    },
    {
      path: '/songslist/:type/:id',
      name: 'songslist-with-tybe',
      component: SongsList
    }
  ]
})
