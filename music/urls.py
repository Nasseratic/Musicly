from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^allSongs/$', views.all_Songs, name='all_Songs'),
    url(r'^song/(?P<song_id>[0-9]+)/$', views.get_songById, name='get_songById'),
    url(r'^allPlaylists/$', views.all_Playlists, name='all_Playlists'),
    url(r'^playlist/(?P<playlist_id>[0-9]+)/$', views.get_playlistById, name='get_playlistById'),
    url(r'^allAlbums/$', views.all_Albums, name='all_Albums'),
    url(r'^album/(?P<album_id>[0-9]+)/$', views.get_albumById, name='get_albumById'),
    url(r'^allArtist/$', views.all_Artists, name='all_Artists'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.get_artistById, name='get_artistById'),
    url(r'^allBands/$', views.all_bands, name='all_Bands'),
    url(r'^band/(?P<band_id>[0-9]+)/$', views.get_bandById, name='get_albumById'),
    url(r'^delBand/(?P<band_id>[0-9]+)/$', views.delete_bandById, name='delete_bandById'),
    url(r'^delSong/(?P<song_id>[0-9]+)/$', views.delete_songById, name='delete_songById'),
    url(r'^delAlbum/(?P<album_id>[0-9]+)/$', views.delete_albumById, name='delete_albumById'),
    url(r'^delArtist/(?P<artist_id>[0-9]+)/$', views.delete_artistById, name='delete_artistById'),
    url(r'^delPlaylist/(?P<playlist_id>[0-9]+)/$', views.delete_playlistById, name='delete_playlistById'),
    url(r'^addBand/$', views.add_band, name='add_band'),
    url(r'^addSong/$', views.add_song, name='add_song'),
    url(r'^addAlbum/$', views.add_album, name='add_album'),
    url(r'^addArtist/$', views.add_artist, name='add_artist'),
    url(r'^addPlaylist/$', views.add_playlist, name='add_playlist'),


]
