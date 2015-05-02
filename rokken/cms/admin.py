from django.contrib import admin
from cms.models import Material, Group, CookingTime, Recipe

class MaterialAdmin(admin.ModelAdmin):
    list_display=('id','name','price',)
    list_display_links=('id','name','price',)
admin.site.register(Material,MaterialAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    list_display_links=('id','name',)
admin.site.register(Group,GroupAdmin)


class CookingTimeAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    list_display_links=('id','name',)
admin.site.register(CookingTime,CookingTimeAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    list_display_links=('id','name',)
admin.site.register(Recipe,RecipeAdmin)
