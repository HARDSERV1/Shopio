from django.shortcuts import render
from .models import Goods
from .forms import NewGoodsForm
# Create your views here.
def index(request):
    goods = Goods.objects.all()
    context = {'goods':goods}
    return render(request,'index.html',context=context)

def new_goods(request):
    form = NewGoodsForm()
    context = {'form':form}
    if request.method=='POST':
        form = NewGoodsForm(request.POST,request.FILES)
        if form.is_valid():
            Goods.objects.create(name=form.cleaned_data['name'],info=form.cleaned_data['info'],image=form.cleaned_data['image'])
            return render(request,'new_goods.html',context)
    return render(request,'new_goods.html',context)