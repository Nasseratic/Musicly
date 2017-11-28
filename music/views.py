
from django.http import JsonResponse,HttpResponse
from .models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple


@csrf_exempt
def all_Songs(request):
    songs = Song.objects.all()
    songs_serialized = serializers.serialize('json',songs)
    return JsonResponse(songs_serialized,safe=False)

def get_songById(request, song_id):
    song = Song.objects.filter(id=song_id)
    song_serialized = serializers.serialize('json', song)
    return JsonResponse(song_serialized, safe=False)

def delete_songById(request, song_id):
    Song.objects.filter(id=song_id).delete()
    return HttpResponse("deletion is done successfully")

@csrf_exempt
def add_song(request):
    if request.method == "POST":
        j = request.body
        x = json.loads(j, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        song = Song.objects.create(name=x.name, path=x.path, releaseDate=x.releaseDate,genre=x.genre,lyrics=x.lyrics,
                                   length=x.length , artist=Artist.objects.filter(id = x.artist)[0])
        song.save()
        #,playlists=x.playlists,bands=x.bands,artist=x.artist
        # playlist= Playlist.objects.filter(id= x.playlist)
        # if x.playlist != None : 
        #     song.playlists.add(playlist)
        if x.album != None :
            Album.objects.filter(id = x.album).song_set(song)
        if x.band != None :
            Band.objects.filter(id = x.band).song_set(song)
        # if x.artist != None :
        #     Artist.objects.filter(id = x.artist)[0].song_set(song)
        
    return HttpResponse("creation is done successfully")




###########################################################
def all_Playlists(request):
    playlists = Playlist.objects.all()
    playlists_serialized = serializers.serialize('json',playlists)
    return JsonResponse(playlists_serialized,safe=False)

def get_playlistById(request, playlist_id):
    playlist = Playlist.objects.filter(id=playlist_id)
    return JsonResponse(serializers.serialize('json', playlist), safe=False)

def delete_playlistById(request, playlist_id):
    Playlist.objects.filter(id=playlist_id).delete()
    return HttpResponse("deletion is done successfully")


@csrf_exempt
def add_playlist(request):
    if request.method == "POST":
        j = request.body
        x = json.loads(j, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        playlist = Playlist.objects.create(name=x.name, description=x.description)
        playlist.save()
    return HttpResponse("creation is done successfully")



#############################################################

def all_Albums(request):
    albums = Album.objects.all()
    albums_serialized = serializers.serialize('json',albums)
    return JsonResponse(albums_serialized,safe=False)

def get_albumById(request, album_id):
    album = Album.objects.filter(id=album_id)
    return JsonResponse(serializers.serialize('json', album), safe=False)

def delete_albumById(request, album_id):
    Album.objects.filter(id=album_id).delete()
    return HttpResponse("deletion is done successfully")


@csrf_exempt
def add_album(request):
    if request.method == "POST":
        j = request.body
        x = json.loads(j, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        album = Album.objects.create(title=x.title, band=x.band)
        album.save()
    return HttpResponse("creation is done successfully")





##############################################################
def all_Artists(request):
    artists = Artist.objects.all()
    return JsonResponse(serializers.serialize('json',artists),safe=False)

def get_artistById(request, artist_id):
    artist = Artist.objects.filter(id=artist_id)
    return JsonResponse(serializers.serialize('json', artist), safe=False)

def delete_artistById(request, artist_id):
    Artist.objects.filter(id=artist_id).delete()
    return HttpResponse("deletion is done successfully")


@csrf_exempt
def add_artist(request):
    if request.method == "POST":
        j = request.body
        x = json.loads(j, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        artist = Artist.objects.create(name=x.name, dateOfBirth=x.dateOfBirth)
        artist.save()
        print(x)
        if x.band != None:
            Band.objects.filter(id= x.band).artist_set(artist)
    return HttpResponse("creation is done successfully")

#############################################################
def all_bands(request):
    bands = Band.objects.all()
    return JsonResponse(serializers.serialize('json',bands),safe=False)

def get_bandById(request, band_id):
    band = Band.objects.filter(id=band_id)
    return JsonResponse(serializers.serialize('json', band), safe=False)

def delete_bandById(request, band_id):
    Band.objects.filter(id=band_id).delete()
    return HttpResponse("deletion is done successfully")


@csrf_exempt
def add_band(request):
    if request.method == "POST":
        j = request.body
        x = json.loads(j, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        band = Band.objects.create(name=x.name)
        band.save()
    return HttpResponse("creation is done successfully")