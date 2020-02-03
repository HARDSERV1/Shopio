from django import forms
from .models import Goods,Photos


class NewGoodsForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = ['image','name','info','current_price','old_price','category']

class PhotosForm(forms.ModelForm):
    class Meta:
        model=Photos
        fields=['location','small_image','big_image']

