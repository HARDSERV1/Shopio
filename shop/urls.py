from django.urls import path
from .views import index,new_goods,add_photos,about_us,cart,RegisterUserView,UserLogin,UserLogout

urlpatterns = [
    path('',index,name='index'),
    path('new_goods',new_goods,name='new_goods'),
    path('add_photos',add_photos,name='add_photos'),
    path('about_us',about_us,name='about_us'),
    path('cart',cart,name='cart'),
    path('sign_up',RegisterUserView.as_view(),name='sign_up'),
    path('sign_in',UserLogin.as_view(),name='sign_in'),
    path('log_out',UserLogout.as_view(),name='log_out')

]