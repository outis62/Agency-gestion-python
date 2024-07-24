from django.shortcuts import render, redirect
from .form import CustomUserCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Créez vos vues ici.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Nom d\'utilisatuer ou mot de passe incorrect.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreateForm()
    return render(request, 'register.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('login')

@login_required
def welcome(request):
    return render(request, 'dashboard/base.html')