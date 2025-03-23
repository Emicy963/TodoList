from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .form import ProfileForm

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()
        return render(request, 'user/register.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')
    
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'user/profile.html', {'form': form})
