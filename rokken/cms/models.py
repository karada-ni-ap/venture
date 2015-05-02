from django.db import models
from django.contrib.auth.models import User

class Material (models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    def __unicode__(self):
        return self.name
        
        
class Group (models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
        
class CookingTime(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
        
                
class Recipe (models.Model):
    name=models.CharField(max_length=200)
    group=models.ForeignKey(Group)
    materials=models.ManyToManyField(Material)
    cookingtime=models.ForeignKey(CookingTime)
    dishes=models.IntegerField()
    website=models.URLField()
    def __unicode__(self):
        return self.name
        

class History(models.Model):
    user=models.ForeignKey(User)
    jump=models.ManyToManyField(Recipe,related_name='jump')
    click=models.ManyToManyField(Recipe,related_name='click')
    login_date=models.DateTimeField('date published')
        


