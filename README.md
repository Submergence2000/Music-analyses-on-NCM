# Singers Lyrics Analyses



## 项目说明

本项目主要用于分析网易云音乐中的歌手和用户的歌曲数据，也可作为歌词的下载工具（只要你乐意），目前已经实现对歌手，专辑，用户以及单曲歌词的爬取及分词（目前仅支持中文歌词和英文歌词），计划在之后实现对**分词结果的字典的数据分析**。由于还没来得及生成配置文件，代码的异常处理也没有做好，而且**所用的第三方库存在一些小的bug**（pull request已经被merge了，可以直接使用。）

开发环境: windows10, python 3.6, vs code



## 文件说明

目前有两个文件比较重要，前者是爬取，后者是生成字典。

```shell
lyrics_crawler.py lyics_analysis.py
```

\my_lib 文件夹下包含了自己写的一些函数以及构造的类，均不涉及IO操作，不用太过在意。

\cache 文件夹下的内容以及data.json和rank.txt的内容为缓存信息以及调试信息，内容并不重要。



## 技术说明

歌手歌曲和专辑歌曲id的爬取是我自己写的爬虫，而用户听过的歌曲id则是使用了现有的python第三方库cloudmusic。

对于中文歌词的分词采用了jieba分词，对英文歌词的分词采用了nltk语言包。



## 计划更新功能

1. 因为现在字典结果中混入了很多不怎么优雅的部分（无意义的词汇，但实际上jieba和nltk分词包都提供词性标注）
2. 词云的生成。

**本项目只供学习交流使用，切勿用于其他用途。**

