# coding: UTF-8

from food import *

class recipe:
  def __init__(self):
    self._exist = True
    self._demand = [0] * nof
  
  def input_name(self, name):
    self._name = name
	
  def input_time(self, time):
    self._time = time
  
  def input_dish(self, dish):
    self._dish = dish
  
  def input_cate(self, category):
    self._category = category
	
  def input_url(self, url):
    self._url = url
  
  def input_food(self, food, amount):
    self._demand[food] = amount
  
  def delete(self):
    self._exist = False

# hoge
# debug
stri = u"約２時間"
print stri[0]
