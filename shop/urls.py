from django.urls import path
from .views import index,new_goods,add_photos

urlpatterns = [
    path('',index,name='index'),
    path('new_goods',new_goods,name='new_goods'),
    path('add_photos',add_photos,name='add_photos')

]