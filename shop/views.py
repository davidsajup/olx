from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Category
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.
def homefn(request):
    p = Product.objects.all()
    c = Category.objects.all()
    return render(request,'home.html',{'pro':p,'category':c})

def searchfn(request):
    x = request.GET['product']
    y=Product.objects.filter(name__icontains = x)
    if y:
        return render(request,'searchresult.html',{'pro':y})
    else:
        return render(request,'searchresult.html',{'er':'No Products Found...'})

def registerfn(request):
    if request.method =='POST':
        u = request.POST['uname']
        f = request.POST['fname']
        l = request.POST['lname']
        em = request.POST['em']
        p1 = request.POST['psw1']
        p2 = request.POST['psw2']

        if p1==p2:
            if User.objects.filter(username = u).exists():
                return render(request,'register.html',{'er':'Username already exists'})
            elif User.objects.filter(email = em).exists():
                return render(request,'register.html',{'er':'Email already exists'})
            else:
                User.objects.create_user(username=u,first_name=f,last_name=l,email=em,password=p1)
                return HttpResponse('User Created Succesfully')
        else:
            return render(request,'register.html',{'er':'Passwords not matching'})

    else:
        return render(request,'register.html')
    
def loginfn(request):
    if request.method == 'POST':
        u=request.POST['uname']
        p1=request.POST['psw1']

        x = auth.authenticate(username=u,password=p1)
        if x:
            auth.login(request,x)
            return redirect('/')
        else:
            return render(request,'login.html',{'er':'Invalid Credentials'})


    return render(request,'login.html')
             
def logoutfn(request):
    auth.logout(request)
    return redirect('/login')

@login_required
def addproductfn(request):
    if request.method =='POST':
        f = ProductForm(request.POST,request.FILES)
        if f.is_valid():
            x=f.save(commit=False)
            x.us=request.user
            x.save()
            return redirect('/')
    
    else:
        f=ProductForm()
        return render(request,'addproduct.html',{'fm':f})
    
def viewcategoryfn(request,cid):
    x = Product.objects.filter(category= cid)
    y=Category.objects.all()
    return render(request,'home.html',{'pro':x,'category':y})

def viewproductfn(request,pid):
    x = Product.objects.filter(id=pid)
    return render(request,'product.html',{'pro':x})

def editproductfn(request,pid):
    product = Product.objects.get(id=pid)

    if product.us != request.user:
        return HttpResponse('Unauthorized Access')
        
    if request.method == 'POST':
        f = ProductForm(request.POST,request.FILES,instance=product)
        if f.is_valid():
            f.save()
            return redirect('/profile/')
    else:
        f = ProductForm(instance=product)
    
    return render(request, 'editproduct.html', {'fm': f})

def deleteproductfn(request,pid):
    x=Product.objects.get(id=pid)
    if request.method == 'POST':
        x.delete()
        return redirect('/profile/')
    else:
        return render(request,'deleteproduct.html')

def profile(request):
    x = Product.objects.filter(us=request.user)
    if x:
        return render(request, 'profile.html', {'pro': x})
    else:
        return render(request, 'profile.html', {'er': 'No Ads!!!'})
    
        
