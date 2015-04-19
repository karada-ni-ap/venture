# coding: UTF-8

f_f = open("syokuzai.txt", "r") #food file
f_l = f_f.readlines() #foods list

nof = len(f_l) #the number of foods

Foods = {} #food dictionary

for i in range(nof):
  ary = f_l[i].split(" ")
  Foods.update({ary[0] : i})

# hoge
