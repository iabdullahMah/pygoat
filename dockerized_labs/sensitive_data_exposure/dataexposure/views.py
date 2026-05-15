from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from .models import UserData
from .forms import UserLoginForm, UserRegisterForm
import random
import string

def index(request):
                     
    return render(request, 'index.html')

def about(request):
                              
    return render(request, 'about.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}! You are now logged in.')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

def generate_api_key():
                               
                                                                  
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=16))                                    

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, password=password)
            
                                                  
                                                               
            UserData.objects.create(
                user=user,
                credit_card='4111111111111111',                             
                ssn='123456789',                       
                api_key=generate_api_key()                                        
            )
            
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
                                             
    try:
        user_data = UserData.objects.get(user=request.user)
                                              
    except UserData.DoesNotExist:
                                                                 
                                                   
        print(f"Creating missing user data for {request.user.username}")                   
        user_data = UserData.objects.create(
            user=request.user,
            credit_card='4111111111111111',                             
            ssn='123456789',                       
            api_key=generate_api_key()                                        
        )
    return render(request, 'profile.html', {'user_data': user_data})

@login_required
def api_data_view(request):
                                                           
                                                  
    try:
        user_data = UserData.objects.get(user=request.user)
    except UserData.DoesNotExist:
                                                                 
        user_data = UserData.objects.create(
            user=request.user,
            credit_card='4111111111111111',                    
            ssn='123456789',            
            api_key=generate_api_key()                  
        )
    
    data = {
        'username': request.user.username,
        'credit_card': user_data.credit_card,
        'ssn': user_data.ssn,
        'api_key': user_data.api_key
    }
                                                       
                                                  
    return JsonResponse(data)

                                                 
def all_users_data_view(request):
                                                                                     
                                       
                                                                             
    
                                                                                      

    all_users_data = []
    for user_data in UserData.objects.all():
        all_users_data.append({
            'username': user_data.user.username,
            'credit_card': user_data.credit_card,                                   
            'ssn': user_data.ssn,                                         
            'api_key': user_data.api_key                                              
        })
    
                                            
                                                                        
                                                                    
    
    return JsonResponse({'users': all_users_data})

def logout_view(request):
                                 
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('index')

def sensitive_data_exposure_lesson(request):
                  
    return render(request, 'lesson.html')
