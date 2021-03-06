import json
import requests
import re
import urllib
import bs4
import cloudmusic
import os

from my_lib.myclass import Crawl_obj, Song, Album, Artist, User
from my_lib.save import lyrics_save

cheat_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def url_reslove(url):
    """目前仅支持网易云音乐链接的解析"""
    crawl_obj = Crawl_obj()

    if re.search(r'.*music.163.com.*', url):
        crawl_obj.site = 'netease'
        crawl_obj.url = re.sub(r'/#', "", url)

        re_url = re.match(r'.*/#/(.*)\?id=(.*)', url)
        if re_url:
            crawl_obj.type = re_url.group(1)
            if crawl_obj.type == "user/home":
                crawl_obj.type = "user"
            
            crawl_obj.id = re_url.group(2)
        else:
            print("Wrong hyperlink formats! ")
    else:
        print("Sorry, this site is not supported! ")

    if crawl_obj.is_incomplete():
        print("The information is incomplete!")
    else:
        return crawl_obj

def crawl_start(crawl_obj):
    """crawl objct and return the result"""
    
    res = None

    if crawl_obj.type in ['user', 'song'] :
        res = eval('crawl_' + crawl_obj.type)(crawl_obj)
    elif crawl_obj.type in ['artist', 'album'] :
        web_data = requests.get(crawl_obj.url, headers = cheat_headers)
        soup = bs4.BeautifulSoup(web_data.text, 'lxml')

        res = eval('crawl_' + crawl_obj.type)(crawl_obj.type, soup)
    else:
        print("Object type UNKNOWN!")
   
    return res

def crawl_artist(crawl_obj, soup):

    name_info = soup.select("#artist-name")
    info = re.match(r'.*>(.*)</h2>', str(name_info))
    items = soup.find('ul', {'class': 'f-hide'}).find_all('a')
    items = (list(items))
    
    artist = Artist(info.group(1))
    for item in items:
        song_name = item.text
        song_id = item.attrs["href"]
        artist.songs.append(Song(song_name, song_id[9:]))
    
    os.chdir("cache/artists")
    if not os.path.exists(os.getcwd() + '/' + artist.name + '/'):
        os.mkdir(os.getcwd() + '/' + artist.name + '/')
    os.chdir(os.getcwd() + '/' + artist.name + '/')
    for index in range(0, len(artist.songs)):
        lyrics_save(artist.songs[index].id)
    #os.chdir("../../../")

    return artist

def crawl_album(crawl_obj, soup):
    
    name_info = soup.select("title")
    info = re.match(r'.*>(.*) - (.*) - (.*) - (.*)<.*', str(name_info))
    items = soup.find('ul', {'class': 'f-hide'}).find_all('a')
    items = (list(items))

    album = Album(info.group(1), info.group(2))
    for item in items:
        song_name = item.text
        song_id = item.attrs["href"]
        album.songs.append(Song(song_name, song_id[9:]))

    os.chdir("cache/albums")
    if not os.path.exists(os.getcwd() + '/' + album.name + '/'):
        os.mkdir(os.getcwd() + '/' + album.name + '/')
    os.chdir(os.getcwd() + '/' + album.name + '/')
    for index in range(0, len(album.songs)):
        lyrics_save(album.songs[index].id)
    #os.chdir("../../../")

    return album

def crawl_song(crawl_obj):
    music = cloudmusic.getMusic(crawl_obj.id)
    song = Song(music.name, crawl_obj.id)

    os.chdir("cache/songs")
    lyrics_save(song.id)
    #os.chdir("../../")

    return song

def crawl_user(crawl_obj):

    temp_user = cloudmusic.getUser(crawl_obj.id)
    music_list = temp_user.getRecord(1)

    user = User(temp_user.nickname, temp_user.id)
    for value in range(0, 100):
        user.songs.append(Song(music_list[value]['music'].name, music_list[value]['music'].id))
    
    os.chdir("cache/users")

    if not os.path.exists(os.getcwd() + '/' + user.name + '/'):
        os.mkdir(os.getcwd() + '/' + user.name + '/')
    
    os.chdir(os.getcwd() + '/' + user.name + '/')
    for index in range(0, len(user.songs)):
        lyrics_save(user.songs[index].id)
    #os.chdir("../../../")

    #user.print_info()
    return user