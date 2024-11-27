from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PlagiarismHistory
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from .utils import calculate_plagiarism  # Our plagiarism function from the helper section

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful!')
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def check_plagiarism(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        ref_text = request.POST['ref_text']
        plagiarism_percentage = calculate_plagiarism(input_text,ref_text)  # Call the helper function
        save_history = 'save_history' in request.POST
        if save_history:
            PlagiarismHistory.objects.create(
                user=request.user,
                input_text=input_text,
                plagiarism_percentage=plagiarism_percentage,
                checked_on=timezone.now()
            )
        return render(request, 'result.html', {'plagiarism_percentage': plagiarism_percentage})
    return render(request, 'check_plagiarism.html')

@login_required
def view_history(request):
    history = PlagiarismHistory.objects.filter(user=request.user).order_by('-checked_on')
    return render(request, 'history.html', {'history': history})

