# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

#Exceptions
from django.db.utils import IntegrityError

# Models

    #User
from django.contrib.auth.models import User

    #Profile
from users.models import Profile 

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        pass_confirm = request.POST['password_confirmation']

        if password != pass_confirm:
            return render(request, 'users/signup.html', {'error': 'Passwords does not match'})

        try:
            user: User = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already exists'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile: Profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def update_profile(request):
    return render(request, 'users/update.html')
