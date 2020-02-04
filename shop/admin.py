from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Goods,Category,Subcategory,Photos
admin.site.register(Goods)
admin.site.register(Photos)
admin.site.register(Subcategory)

class CollectionAdmin(admin.ModelAdmin):
    filter_horizontal = ('sub_category',)


admin.site.register(Category, CollectionAdmin)