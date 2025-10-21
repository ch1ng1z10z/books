from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
@login_required
def profile(request):
    user = request.user
    initials = f"{user.first_name[0]}.{user.middle_name[0] if user.middle_name else ''}.{user.last_name[0]}"
    return render(request, 'accounts/profile.html', {'initials': initials})