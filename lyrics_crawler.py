from my_lib.crawler import url_reslove, crawl_start
from my_lib.myclass import Crawl_obj, Song, Artist

#这里需要输入一个想要爬取内容的url(可以为歌手，专辑，或者某一首歌的链接), 具体请STFW.
crawl_obj_url = input("Please input the url of the object you want to crawl: ")

#返回的obj包括类型(歌手/歌单/歌曲), ID, 链接, 以及网站(目前仅支持网易云)
crawl_obj = url_reslove(crawl_obj_url)
#crawl_obj.print_info()

ret_val = crawl_start(crawl_obj)
