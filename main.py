# coding: UTF-8

from food import *
from recipe import *
from make_table import *
from matching import *

# インポートは
# food.py → recipe.py → make_table.py → matching.py の順

# debug
for i in range(nor):
  print Recipes[i].name
  print Recipes[i].demand
  
user = [0, 20, 0, 0, 0, 0, 0, 10, 0, 0, 50]
order = search(user, Recipes)
print order

#hoge
