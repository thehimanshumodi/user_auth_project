from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login') # Redirect to login page after successful signup
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.replace('_', ' ').title()}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.first_name}!')
                # Redirect based on user type
                if user.user_type == 'Patient':
                    return redirect('patient_dashboard')
                elif user.user_type == 'Doctor':
                    return redirect('doctor_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url='login')
def patient_dashboard_view(request):
    if request.user.user_type != 'Patient':
        messages.error(request, 'Access denied. You are not a patient.')
        return redirect('login') # Or some other appropriate redirect
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})

@login_required(login_url='login')
def doctor_dashboard_view(request):
    if request.user.user_type != 'Doctor':
        messages.error(request, 'Access denied. You are not a doctor.')
        return redirect('login') # Or some other appropriate redirect
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')