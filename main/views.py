from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from main.forms import SignupForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from main.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import requests


# Simple page views
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def products(request):
    return render(request, 'main/products.html')

def benifits(request):
    return render(request, 'main/benifits.html')   # using your filename
def ingredient(request):
    return render(request, 'main/ingredient.html')
def ereview(request):
    return render(request, 'main/ereview.html')
def testimonial(request):
    return render(request, 'main/testimonial.html')
def blog(request):
    return render(request, 'main/blog.html')
def contact(request):
    return render(request, 'main/contact.html')
@login_required
def cart(request):
    return render(request, 'main/cart.html')
def products(request):
    data = Product.objects.all()
    return render(request, 'main/products.html', {'products': data})

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

def dataview(request):
    res=requests.get( 'http://127.0.0.1:8000/product/')
    data=res.json()
    return render(request, 'main/data.html', {'d':data})

# view1..view12
def view1(request): return render(request, 'main/view1.html')
def view2(request): return render(request, 'main/view2.html')
def view3(request): return render(request, 'main/view3.html')
def view4(request): return render(request, 'main/view4.html')
def view5(request): return render(request, 'main/view5.html')
def view6(request): return render(request, 'main/view6.html')
def view7(request): return render(request, 'main/view7.html')
def view8(request): return render(request, 'main/view8.html')
def view9(request): return render(request, 'main/view9.html')
def view10(request): return render(request, 'main/view10.html')
def view11(request): return render(request, 'main/view11.html')
def view12(request): return render(request, 'main/view12.html')

def logout_view(request):
    logout(request)
    return redirect('/index')

def signup_view(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'main/register.html', {'f':form})



