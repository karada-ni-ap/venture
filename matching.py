# coding: UTF-8

from make_table import *

def search(user, Recipes):
  #引数userはユーザーが消費したい食材のリスト

  compare = [0] * nor #各レシピの優先度を格納するリスト
  for i in range(nor):
    for j in range(nof):
      if Recipes[i].demand[j] <= user[j]: #【ToDo】何人前作るのかにも対応させる
        compare[i] += 1
  
  #【debug】compareはうまく入ってる
  
  order = [-1] * nor #優先度順にレシピのindexを並べたリスト
  maxi = -1
  i = 0 #現在注目している順位
  
  while True:
    maxi = max(compare) #優先度の最大値
    if maxi == 0:
      break
    
    index = compare.index(maxi) #最大値が格納されているindex
    compare[index] = 0 # 0に更新
    order[i] = index # i番目に優先度が高いレシピをorderのi番目に格納
    i += 1
  
  return order

#hoge
