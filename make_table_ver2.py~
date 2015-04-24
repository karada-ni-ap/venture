# coding: UTF-8

from food import *
from recipe import *

ue_file  = open("ue2.txt", "r")
ue_lines = ue_file.readlines()

st_file  = open("st2.txt", "r")
st_lines = st_file.readlines()

nor = len(ue_lines) / 2 #the number of recipes

Recipes = [] #レシピのテーブル

for i in range(nor):
  Recipes += [recipe()]
#【Memo】
# Recipes = [recipes()] * nor と宣言すると
# 同じオブジェクトをnor個持つリストになってしまう

for i in range(nor): # i = 0, 1, ... , nor-1
  ary1 = ue_lines[2*i].split(" ") #単語ごとに区切られた配列
  
  Recipes[i].input_name(ary1[0])
  Recipes[i].input_time(ary1[1])
  Recipes[i].input_cate(ary1[3])
  
  dish = int(ary1[2])
  if dish >= 1 and dish <= 10:
    Recipes[i].input_dish(ary1[2])
  else:
    Recipes[i].delete
  
  ary2 = ue_lines[2*i+1].split(" ")
  Recipes[i].input_url(ary2[0])
    
  ary3 = st_lines[2*i]
  ary4 = st_lines[2*i+1]
  
  if len(ary3) == len(ary4):
    bound = ( len(ary) - 1 ) #注目しているレシピに必要な食材の種類
    
    for j in range(bound): # j = 0, 1, ... , bound-1
      Recipes[i].input_food( Foods[ ary3[j] ], ary4[j] )
      
  else:
    Recipes[i].delete

#hoge
