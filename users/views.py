from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required #This decorator is required for profile funtion to behave in a particular manner explained futhr
from .forms import UserRegisterForm #pre-built UserCreationForm has been replaced now and we have our own form

#So with the below fn new user account has been created, 
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

#We need to restrict users to certain routes when they are logged in and logged out eg, profile route so,
#Adding the below decorator provides a check, that a user must definetely be logged in to view this page
#If this is not added then everything would work fine, howevr when /profile is manually routed then it opens the page but displays nothing
#Still the below only restricts to manually open the /profile and gives 404 error, to drive to login page edit settings.py

@login_required
def profile(request):
    return render(request, 'users/profile.html')


