# -*- coding:utf-8 -*-
##########↑はおまじない！

##########urllib2はurlにつなぐのに利用している。Beautifulsoapは読み取るのに利用している。
import urllib2
from bs4 import BeautifulSoup

##########まず読み取った内容を記述するsource.txtを作成(開く)
f=open('source1.txt','w')

##########iはURlの下3桁に相当。１００～１９８で取れるデータを取る。
i=100
while i < 199:
	############楽天レシピのページはランダムで存在しないことがあるので、ページが存在せず４０４エラーが出た時はexceptに飛ぶ	
	try:
		###########urlを開き、soupにHTMLデータを全部読み込む。nameはHTMLデータのうち料理名に相当する部分。	
		url=urllib2.urlopen("http://recipe.rakuten.co.jp/recipe/1730006"+str(i)+"/")	
		soup=BeautifulSoup(url)
		name=soup.find("h1",itemprop="name")
		###########HTMLデータで料理名と思える部分が二つ以上ある場合は破棄。
		###########HTMLデータで、materialは材料名、amountは分量と思われる部分。これらはリスト。
		if len(name)==1:
			material=soup.find_all(id="material_link")
			amount=soup.find_all(class_="amount")
			
			##########材料の数と分量の数が合わない場合は破棄。
			##########料理名　改行　材料達(空白区切り)　改行　分量(空白区切り)　でsource.txtに書き込み。　
			if len(material)==len(amount):
				name=name.string
				f.write(name.encode("utf8"))
				f.write("\n")

				for k in range(len(material)):
					material[k]=material[k].string
					f.write(material[k].encode("utf8"))
					f.write(" ")
				f.write("\n")
				for k in range(len(amount)):
					amount[k]=amount[k].string
					f.write(amount[k].encode("utf8"))
					f.write(" ")
				f.write("\n")
				
			i+=1
	##########４０４エラーの場合は、読み取ることなく次のページ(i+)に進む。
	except:
		i+=1
	
###########whileループが終わったらsource.txtを閉じて終了。
f.close




####################課題####################
##########現状、「醤油、マヨネーズ　少量」みたいに一つの欄に二つの材料が入ってしまっているのがある。
##########現状、分量に単位がある(大丈夫なのだろうか)。
##########現状、材料名や分量の単位や何人前かが統一されていない(レシピを投稿している人それぞれ)
##########他にもあると思うのでお願いします。

