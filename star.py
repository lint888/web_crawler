from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as bf
import matplotlib.pyplot as plt

html = urlopen("https://www.baidu.com")
obj = bf(html.read(),'html.parser')
pic_info = obj.find_all('img',class_="index-logo-src")
logo_url = "https:" + pic_info[0]['src']
urlretrieve(logo_url,'logo.png')
