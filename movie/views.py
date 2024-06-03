from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            # Handle password mismatch
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'signup.html')