from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm #pre-built UserCreationForm has been replaced now and we have our own form

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #for a post request validating data from here
        if form.is_valid():
            form.save()  #Saving the user, also hashes pwd and does all backend stuff
            username = form.cleaned_data.get('username') #username data will be in the cleaned_data dictionary
            messages.success(request, f'Your account has been created! You are now able to log in') 
            #after the above the user has to be redirected to the next page(now login page) so her we go, 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#So with the abovve new user account has not really been created, 
#however we know that our forms are validating data and responding.
