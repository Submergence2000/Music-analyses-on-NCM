import os
import cloudmusic
import re

def name_stdize(name_init):

    name = name_init + ".txt"
    for symbol in [r'\\', r'/', r':', r'\*', r'"', r'<', r'>', r'\|', r'\?'] :
        name = re.sub(symbol, " ", name)
    
    return name

def lyrics_stdize(lyrics_init):

    lyrics = re.sub(r'\[.*\]', "", lyrics_init)

    #print(lyrics)
    return lyrics

def lyrics_save(music_id):
    song = cloudmusic.getMusic(music_id)
    name = name_stdize(song.name)
    lyrics = lyrics_stdize(song.getLyrics()[0])
    #print(lyrics)
    file = open(name, 'w', encoding='utf-8')
    file.write(lyrics)
    file.close()

"""while 1:
    tst = input()
    lyrics_save(tst)"""