from django.urls import path
from .views import index,new_goods,add_photos,about_us,cart

urlpatterns = [
    path('',index,name='index'),
    path('new_goods',new_goods,name='new_goods'),
    path('add_photos',add_photos,name='add_photos'),
    path('about_us',about_us,name='about_us'),
    path('cart',cart,name='cart')

]