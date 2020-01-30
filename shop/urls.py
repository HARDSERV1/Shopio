from django.urls import path
from .views import index,new_goods

urlpatterns = [
    path('',index,name='index'),
    path('new_goods',new_goods,name='new_goods')
]