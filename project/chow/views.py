from django.shortcuts import render,redirect
from chow.forms import CustomUserForm,CustomDishes
from chow.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



def home(request):
   dishes=Product.objects.filter(is_featured=1)
   return render(request,"chow/home.html",{"dishes":dishes})
def index(request):
    return render(request,"chow/index.html")
def register(request):
    return render(request,"chow/register.html")
def fare(request):
  cuisines=Menu.objects.filter(status=0)
  return render(request,"chow/menu.html",{"cuisines":cuisines})
 
def menucard(request,name):
  if(Menu.objects.filter(name=name,status=0)):
      dishes=Product.objects.filter(category__name=name)
      return render(request,"chow/home.html",{"dishes":dishes,"menu_name":name})
  else:
    messages.warning(request,"No such Cuisine found!")
    return redirect('menu')

def dishlist(request,sname,dname):
    if(Menu.objects.filter(name=sname,status=0)):
      if(Product.objects.filter(name=dname,status=0)):
        dishes=Product.objects.filter(name=dname,status=0).first()
        return render(request,"chow/dish.html",{"dishes":dishes})
      else:
        messages.error(request,"No Such Sustenance Found!")
        return redirect('menu')
    else:
      messages.error(request,"No Such Dietary Classification Found!")
      return redirect('menu')
    


def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")

def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"chow/login.html")

def register(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"You have successfully joined 'The Chow Bear'!")
      return redirect('/login')
  return render(request,"chow/register.html",{'form':form})
    
def custom(request):
    if request.method=='POST':
      order=CustomDishes(request.POST,request.FILES)
      if order.is_valid():
        order.save()
        return render(request,"chow/order.html")
    else:
      order=CustomDishes()
      return render(request,"chow/custom.html",{'order':order})

