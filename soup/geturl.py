# -*- coding:utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup

#preurl.txtとurl.txtファイルを開く
f=open('url.txt','w')
g=open('preurl.txt','r')

line=g.readline()
line=line.strip("\n")

#urlを入力しhtmlコード取得
while line:
    line="http://recipe.rakuten.co.jp"+line
    url=urllib2.urlopen(line)
    soup=BeautifulSoup(url)

    #ジャンルの取得
    genre=soup.find("strong",itemprop="title")
    genre=genre.string
    f.write(genre.encode("utf8"))
    f.write("\n")

    #レシピのランキング20傑のurl取得
    for link in soup.find_all(href=re.compile("/recipe/"),id=True):
        f.write("http://rakuten.co.jp")
        f.write(link.get('href'))
        f.write("\n")
        
    line=g.readline()
    f.write("nittaceo\n")
    
f.write("nomacto\n")       
f.close
g.close
