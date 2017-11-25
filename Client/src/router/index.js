import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home'
import Playlists from '@/components/playlists'
import Artists from '@/components/artists'

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
    }
  ]
})
