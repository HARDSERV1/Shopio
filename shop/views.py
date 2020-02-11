from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.files.base import ContentFile
from .models import Goods,Photos,Category,Subcategory,User
from .forms import NewGoodsForm,PhotosForm,RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    value = ''
    all_goods = Goods.objects.all()
    catalog = {}
    for i in Goods.objects.all():
        catalog[i] = [{'good':i},{'category':i.category},{'sub_category':i.sub_category}]


    photos = Photos.objects.all()
    context = {'all_goods':all_goods,
               'catalog':catalog,
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
                                        sub_category=form.cleaned_data['sub_category']
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



def about_us(request):
    return render(request,'about_us.html')

def cart(request):
    return render(request,'cart.html')

class UserLogin(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')

class UserLogout(LoginRequiredMixin,LogoutView):
    template_name = 'logout.html'

class RegisterUserView(CreateView):
    model=User
    template_name = 'sign_up.html'
    form_class=RegisterUserForm
    success_url = reverse_lazy('index')
