from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm, CustomerForm
from .models import Product, Customer


def home(request):
    return render(request, 'home.html', {})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def product_details(request):
    return render(request, 'product_details.html', {})

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new User object
            user = User.objects.create_user(username=form.cleaned_data['email'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            
            # Create a new Customer linked to the User
            customer = Customer(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                id_number=form.cleaned_data['id_number'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                password=form.cleaned_data['password1'],
                date_of_birth=form.cleaned_data['birthdate']
            )
            customer.save()
            
            # Log the user in
            login(request, user)
            messages.success(request, "Registro exitoso!")
            return redirect('home')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión correcto!")
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Sesión finalizada")
    return redirect('home')

def profile_view(request):
    customer = request.user.customer

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to profile after saving
    else:
        form = CustomerForm(instance=customer)
    
    context = {
        'form': form
    }
    return render(request, 'profile.html', context)