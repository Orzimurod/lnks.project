from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from apps.lnks_app.models import Click, Link
from apps.utils import generate_short_code
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required


def home_view(request):
    context={
        'url': ''
    }
    if request.method =='POST' and request.user.is_authenticated:
        original_url = request.POST.get('original_url')
        short_code=generate_short_code()
        link=Link.objects.create(original_url=original_url,short_code=''.join(short_code),user=request.user)
        link.save()
        context['url']=f'http://localhost:8000/{link.short_code}/'
        
    return render(request, 'index.html' ,context=context)

def redirect_view(request, short_code):
    link = Link.objects.filter(short_code=short_code)
    if link.exists():
        click=Click.objects.create(link=link.first())
        click.save()
        return redirect(link.first().original_url)
    return render(request, '404.html')

def login_view(request):
    return render(request,'login.html')
    

def logout_view(request):
    logout(request) 
    return redirect('home')

def register_view(request):
    return render(request,'register.html')

@login_required(login_url='login')
def my_links(request):
    user = request.user
    links=Link.objects.filter(user=user).order_by('-id')
    return render(request,'lnks.html',{'links':links})