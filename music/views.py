
from django.http import JsonResponse
from .models import *
from django.core import serializers


def all_Songs(request):
    songs = Song.objects.all()
    songs_serialized = serializers.serialize('json',songs)
    return JsonResponse(songs_serialized,safe=False)

def get_songById(request, song_id):
    song = Song.objects.filter(id=song_id)
    song_serialized = serializers.serialize('json', song)
    return JsonResponse(song_serialized, safe=False)

###########################################################
def all_Playlists(request):
    playlists = Playlist.objects.all()
    playlists_serialized = serializers.serialize('json',playlists)
    return JsonResponse(playlists_serialized,safe=False)

def get_playlistById(request, playlist_id):
    playlist = Playlist.objects.filter(id=playlist_id)
    return JsonResponse(serializers.serialize('json', playlist), safe=False)

#############################################################

def all_Albums(request):
    albums = Album.objects.all()
    albums_serialized = serializers.serialize('json',albums)
    return JsonResponse(albums_serialized,safe=False)

def get_albumById(request, album_id):
    album = Album.objects.filter(id=album_id)
    return JsonResponse(serializers.serialize('json', album), safe=False)

##############################################################
def all_Artists(request):
    artists = Artist.objects.all()
    return JsonResponse(serializers.serialize('json',artists),safe=False)

def get_artistById(request, artist_id):
    artist = Artist.objects.filter(id=artist_id)
    return JsonResponse(serializers.serialize('json', artist), safe=False)

#############################################################
def all_bands(request):
    bands = Band.objects.all()
    return JsonResponse(serializers.serialize('json',bands),safe=False)

def get_bandById(request, band_id):
    band = Band.objects.filter(id=band_id)
    return JsonResponse(serializers.serialize('json', band), safe=False)