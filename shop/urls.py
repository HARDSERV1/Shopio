from django.urls import path
from .views import index,new_goods,about_tovar

urlpatterns = [
    path('',index,name='index'),
    path('new_goods',new_goods,name='new_goods'),
    path('new_goods/<int:pk>',about_tovar,name='about_tovar')
]