# -*- coding:utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup

#preurl.txtファイルを開く
f=open('preurl.txt','w')

i=30

#urlを入力しhtmlコード取得
while i<34:
    try:
        url=urllib2.urlopen("http://recipe.rakuten.co.jp/category/"+str(i)+"/")
        soup=BeautifulSoup(url)
    
        for link in soup.find_all(href=re.compile("/category/"+str(i)+"-")):
            if len(link.get('href'))<=17:
                f.write(link.get('href'))
                f.write("\n")

        i+=1
        
    except:
        i+=1
f.close

#ソート
f=open('preurl.txt','r')
lines=f.readlines()
f.close

lines.sort()

f=open('preurl.txt','w')
for line in lines:
    f.write(line)
f.close
