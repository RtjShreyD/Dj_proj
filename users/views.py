from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required #Importing login_required decorator
from .forms import UserRegisterForm 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()  
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your Account has been created, You can login now') 
            
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  #Builtin Django Decorator to put a check on opening the profile page manually if user is not logged in
def profile(request):
    return render(request, 'users/profile.html')
