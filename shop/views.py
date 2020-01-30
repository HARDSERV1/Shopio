from django.shortcuts import render,redirect
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
    if request.method == 'POST':
        form = NewGoodsForm(request.POST, request.FILES)
        if form.is_valid():
            good = Goods.objects.create(name = form.cleaned_data['name'],
                                        image=form.cleaned_data['image'],
                                        current_price = form.cleaned_data['current_price'],
                                        old_price = form.cleaned_data['old_price'],
                                        info = form.cleaned_data['info']
                                        )
            return redirect('index')
    return render(request,'new_goods.html',context)

def about_tovar(request,pk):
    goods = Goods.objects.all()
    tovar = Goods.objects.get(pk=pk)
    return render(request,'about_tovar.html',{'tovar':tovar,'goods':goods})
