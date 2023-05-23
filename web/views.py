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
from .models import Product

def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def shop(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'web/shop.html', context)

def single_page(request,id):
    product = get_object_or_404(Product,id=id)
    context = {"product": product}
    return render(request, 'web/single_page.html', context)




from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('web:shop')
        else:
            messages.error(request, 'Invalid email or password.')

    
    return render(request, 'web/login.html')



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
            context['error'] = 'Passwords do not match'
            context['email'] = email  # Save the email in the context
            return render(request, 'web/signup.html', context)
        else:
            username = email
            if User.objects.filter(email=email).exists():
                print('User already exists')
                context['error'] = 'User already exists'
                context['email'] = email  # Save the email in the context
                return render(request, 'web/signup.html', context)
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                context['email'] = email  # Save the email in the context
                return redirect('web:login')

    return render(request, 'web/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('web:shop')


def about(request):
    context = {}
    return render(request, 'web/about-us.html', context)


def contact(request):
    context = {}
    return render(request, 'web/contact-us.html', context)


