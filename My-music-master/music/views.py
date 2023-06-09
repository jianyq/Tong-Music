from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import AlbumForm, SongForm, UserForm
from .models import Album, Song
from django.views.decorators import csrf
#-*- version: Python3.0 -*
#-*- coding: UTF-8      -*
from . import generate, speech_to_singing, add_data
import urllib
import urllib.request
import sys
import ssl
import requests
import json
import random
from wxpy import *
AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MsGjEykNWRrG2HBcYfvy0jMl&client_secret=rDjZyBWmEH7PIjtP8hbKYnXExmzxjw3M'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
resp_taken = response.read()
 
#if (resp_taken):
#    print(resp_taken)
 
text = json.loads(resp_taken)
#print(text["access_token"])
 
headers = {'Content-Type':'application/json'}
access_token = text["access_token"]
url = 'https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=' + access_token

def baiduApi1(mas):
    t = mas
    post_data = "{\"log_id\":\"953d27b0-5d3e-11ea-9880-67be6768f9b5\",\"version\":\"2.0\",\"service_id\":\"S27580\",\"session_id\":\"service-session-id-1583233395694-3574416c09ff433ab5a3006f1de85a33\",\"request\":{\"query\":\"" + t + "\",\"user_id\":\"88888\"},\"dialog_state\":{\"contexts\":{\"SYS_REMEMBERED_SKILLS\":[\"1057\"]}}}"
    request = urllib.request.Request(url,data=post_data.encode('utf-8'),headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    text1 = json.loads(content)
    return text1['result']['response_list'][0]['action_list'][0]['say']

def create_album(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']
            file_type = album.album_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/create_album.html', context)
            album.save()
            return render(request, 'music/detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'music/create_album.html', context)


def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/create_song.html', context)

        song.save()
        return render(request, 'music/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'albums': albums})


def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})


def detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'music/detail.html', {'album': album, 'user': user})


def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'albums': albums,
                'songs': song_results,
            })
        else:
            return render(request, 'music/index.html', {'albums': albums})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def songs(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })


def qna(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        ctx ={}
        textt = request.GET.get("qna")
        if textt:
            textt = textt.replace(" ","").replace("\n","")
            if textt:
                textt = baiduApi1(textt)
                ctx['rlt'] = textt
            else:
                ctx['rlt'] = '你刚才说啥了？？？？？'
        return render(request, 'music/qna.html', ctx)

def proses(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        ctx ={}
        ctx['res'] = 'Please input the lyrics.'
        ctx['song_str'] = 'Please input the song title.'
        ctx['album_str'] = 'Please input the album name.'
        textt = request.GET.get("prose")
        lyricc = request.GET.get("lyric")
        song_title = request.GET.get("song_name")
        album_name = request.GET.get("album_name")
        if textt:
            for i in range(1,6):
                label = 'rlt' + str(i)
                text_out = generate.main(textt)
                
                ctx[label] = text_out
        if lyricc:
            ctx['res'] = 'Good job!'
        if song_title:
            ctx['song_str'] = 'Good job!'
        if album_name:
            ctx['album_str'] = 'Good job!'
        if lyricc and song_title and album_name:
            beat_file_path = 'E:/Tong-music/raprapraprap/GPT2/beat.mp3'
            tmp_file_path = 'E:/Tong-music/raprapraprap/GPT2/test.mp3' 
            out_putpath = 'E:/Tong-music/机器学习和数据挖掘在说唱歌词生成中的应用/2-参赛作品/My-Music-master/media/' + song_title + '.mp3' 
            success_num = add_data.add_AI_song(song_title, album_name)
            if success_num:
                speech_to_singing.create(lyricc, beat_file_path, tmp_file_path, out_putpath)
                
                ctx['res'] = 'AI-ROBOT finshes creating!!!'
        return render(request,'music/proses.html',ctx)
