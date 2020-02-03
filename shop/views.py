from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.files.base import ContentFile
from .models import Goods,Photos
from .forms import NewGoodsForm,PhotosForm
# Create your views here.
def index(request):
    value = ''
    all_goods = Goods.objects.all()
    speaker_goods = Goods.objects.filter(category='Speaker')
    TV_goods = Goods.objects.filter(category='Tv & Audio')
    mobile_goods = Goods.objects.filter(category='Mobile')
    photos = Photos.objects.all()
    context = {'all_goods':all_goods,
               'speaker_goods':speaker_goods,
               'TV_goods':TV_goods,
               'mobile_goods':mobile_goods,
               'photos':photos,
               'value':value}
    return render(request,'index.html',context=context)

def new_goods(request):
    form = NewGoodsForm()

    context = {'form':form,}
    if request.method == 'POST':
        form = NewGoodsForm(request.POST, request.FILES)
        if form.is_valid():
            good = Goods.objects.create(name = form.cleaned_data['name'],
                                        image=form.cleaned_data['image'],
                                        current_price = form.cleaned_data['current_price'],
                                        old_price = form.cleaned_data['old_price'],
                                        info = form.cleaned_data['info'],
                                        category=form.cleaned_data['category'],
                                        )


            return redirect('index')
    return render(request,'new_goods.html',context)

def add_photos(request):
    form = PhotosForm()
    goods = Goods.objects.all()
    context = {'form': form,'goods':goods}
    if request.method=='POST':
        form =  PhotosForm(request.POST, request.FILES)
        if form.is_valid():
            photo = Photos.objects.create(small_image=form.cleaned_data['small_image'],big_image=form.cleaned_data['big_image'],location=form.cleaned_data['location'])
            return redirect('index')
    return render(request,'add_photos.html',context)





