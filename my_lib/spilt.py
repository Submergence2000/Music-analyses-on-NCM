import jieba
import jieba.posseg
import nltk
import os
import math

ret_dict = dict()
zh_block_list = ['u', 'c']
en_block_list = ['VBZ', 'DT', 'CC', 'TO', 'DT', 'IN']
nonsense = ["n't", '：', ':', '/', "'m", 'oh', '是', 'be', '.', 'up', '作词', \
            '作曲', 'so', 'up', 'be', '这', '也', 'just', '那', '把', 'wan', 'are'\
            '都', '还', '~', '，', 're', "'ll", '会', 'was', 'ca', "'s", "编曲", '@' ]

def lan_zh(s):
    """check whether s contains a Chinese character"""

    flag = 0

    for char in s:
        if '\u4e00' <= char <= '\u9fff' or '\u0000' <= char <= '\u0100':
            if '\u4e00' <= char <= '\u9fff':
                flag = 1
        elif '\u2000'<= char <= '\u206f' or '\u3000'<= char <='\u303f' \
                or '\uff00'<= char <='\uffef':
            pass
        else:
            return -1
    
    return flag

def zh_spilt(line):
    words = jieba.posseg.cut(line)
    for word, flag in words:
        if (flag[0] not in zh_block_list) and word != " ":
            if word in ret_dict:
                ret_dict[word] = ret_dict[word] + 1
            else:
                ret_dict[word] = 1

def en_spilt(line):
    words = nltk.word_tokenize(line)
    words = nltk.pos_tag(words)
    for index in range(0, len(words)):
        if words[index][1] not in en_block_list and len(words[index][0]) != 1:
            word = words[index][0].lower()
            if word in ret_dict:
                ret_dict[word] = ret_dict[word] + 1
            else:
                ret_dict[word] = 1

def spilt_lyrics(name):

    file = open(name, 'r', encoding='utf-8')

    ret_dict.clear()
    for line in file:
        line = line.rstrip()
        p = lan_zh(line)
        if(p == 1):
            zh_spilt(line)
        elif(p == 0):
            en_spilt(line)
        else:
            pass
    
    for bullshit in nonsense:
        if bullshit in ret_dict:
            del ret_dict[bullshit]

    return ret_dict

def dict_adjust(a_dict):

    for key, value in a_dict.items():
        if value >= 15:
            a_dict[key] = round(math.log(value, 1.2))

    return a_dict
