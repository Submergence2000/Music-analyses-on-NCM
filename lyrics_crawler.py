import json
import os

from my_lib.crawler import url_reslove, crawl_start
from my_lib.myclass import Crawl_obj, Song, Artist

#这里需要输入一个想要爬取内容的url(可以为歌手，专辑，或者某一首歌的链接), 具体请STFW.
crawl_obj_url = input("Please input the url of the object you want to crawl: ")
origin_path = os.getcwd() 
#返回的obj包括类型(歌手/歌单/歌曲), ID, 链接, 以及网站(目前仅支持网易云)
crawl_obj = url_reslove(crawl_obj_url)

ret_val = crawl_start(crawl_obj)

print("\nAll lyrics have been download and standardize in the cache folder!")
print("If you have other lyrics to analyze, please store it in the corresponding folder!")
print("\nP.S. If you want to standardize the lyrics you download, the 'lib\\save.py' may help you!")
print("\nThe object that you crawl: ")
print("name: " + ret_val.name)

data = dict()
data['path'] = os.getcwd()
data['name'] = ret_val.name

with open(origin_path + "\\data.json", 'w', encoding='utf-8') as f:
    json.dump(data, f)

os.chdir(origin_path)

print("\nThe data of the object has been saved successfully!")