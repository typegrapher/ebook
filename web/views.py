from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def shop(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'web/shop.html', context)

def single_page(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, 'web/product-details.html', context)





def Login(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('web:shop')
        else:
            print('invalid details')
            return redirect('web:shop')

    return render(request, 'web/login.html', context)


def signup(request):
    context = {}
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            print('Passwords do not match')
            return redirect('web:signup_view')
        else:
            username = fname + lname
            if User.objects.filter(email=email).exists():
                print('User already exists')
                return redirect('web:login')
            else:
                user = User.objects.create_user(email=email, password=password)
                return redirect('web:login')

    return render(request, 'web/signup.html', context)



def about(request):
    context = {}
    return render(request, 'web/about-us.html', context)


def contact(request):
    context = {}
    return render(request, 'web/contact-us.html', context)


