from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # This is a pre-built form template in django
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #for a post request validating data from here
        if form.is_valid():
            username = form.cleaned_data.get('username') #username data will be in the cleaned_data dictionary
            messages.success(request, f'Account created for { username }!') 
            #after the above the user has to be redirected to the next page(home page here) so her we go, 
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

#So with the abovve new user account has not really been created, 
#however we know that our forms are validating data and responding.
