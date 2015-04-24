# coding: UTF-8

from food import *
from recipe import *

r_f = open("reading.txt", "r") #recipe file
r_l = r_f.readlines() #recipe list

nor = len(r_l) #the number of recipes

Recipes = [] #レシピのテーブル

for i in range(nor):
  Recipes += [recipe()]
#【Memo】
# Recipes = [recipes] * nor と宣言すると
# 同じオブジェクトをnor個持つリストになってしまう

for i in range(nor): # i = 0, 1, ... , nor-1
  ary = r_l[i].split(" ") #単語ごとに区切られた配列
  
  Recipes[i].input_name(ary[0])
  
  bound = ( len(ary) - 1 ) / 2 #注目しているレシピに必要な食材の種類
  for j in range(bound): # j = 0, 1, ... , bound-1
    Recipes[i].input_food( Foods[ ary[2*j+1] ], int(ary[2*j+2]) )

#hoge
