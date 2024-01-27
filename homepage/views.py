from django.shortcuts import render, redirect
from  django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from .models import Profile, Cart, Product
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index (request):
    return render (request, 'homepage/index.html')

def page (request):
    return render (request, 'homepage/page.html')

def loginpage (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Either username or password is incorrect!') 
    return render (request, 'homepage/login.html')

def register (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            Profile.objects.create(username=username, email=email)
            messages.warning(request, f'Account created successfully for {username}.')
            return redirect('/login/')
        else:
            print('it was not successfull')
    else:
        form = RegisterForm()
    return render (request, 'homepage/register.html', {'form':form})

def logoutpage(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('/login/')

@login_required(login_url='/login/')
def homepage(request):
    product_six_data_entry  = Product.objects.filter()[:6]
    count = product_six_data_entry.count()
    numberOfItemInCart = Cart.objects.all().count()
    context = {
    
        'product_six_data_entry': product_six_data_entry,
        'count': count,
        'numberOfItemInCart':numberOfItemInCart
    }

    if request.method == 'POST':
        add_to_cart = request.POST['add_to_cart']
        if add_to_cart:
            product_name =  request.POST['product_name']
            product_price =  request.POST['product_price']
            product_image =  request.POST['product_image']
            product_quantity =  request.POST['product_quantity']
            if_product_exist_in_cart = Cart.objects.filter(name = product_name)
            cart_product_count =  if_product_exist_in_cart.count()
            if cart_product_count > 0:
                messages.info(request, 'already added to cart!')
            else:
                Cart.objects.create(profile = 
                                        Profile.objects.get(username = request.user.username),
                                    name = product_name, 
                                    price = product_price, 
                                    quantity= product_quantity,
                                    image= product_image)
                messages.info(request, 'product added to cart!')
                return redirect('/')
   
    
    return render(request, 'homepage/homepage.html', context)

@login_required(login_url='/login/')
def about (request):
    numberOfItemInCart = Cart.objects.all().count()    
    context = {
        'numberOfItemInCart':numberOfItemInCart
    }
    return render(request, 'homepage/about.html', context)


def layout(request):
    
    numberOfItemInCart = Cart.objects.all().count()    
    context = {
        'numberOfItemInCart':numberOfItemInCart
    }
    return render(request, 'homepage/layout.html', context)
