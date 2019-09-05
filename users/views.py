from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required #Importing login_required decorator
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 

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

@login_required  #Built-in Django Decorator to put a check on opening the profile page manually if user is not logged in
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                 instance=request.user) #creating instances of the forms here
        
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile) 
    #Along with the form data there will be additional data ie, pics so it is file data, 
    #has to be passed above before instance to be acknowledged 

        if u_form.is_valid() and p_form.is_valid():  #Check validity and save the form data to DB
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated !') 
            return redirect('profile')
            #it is being redirected above to profile instead of going to return render below,
            #becoz of something called "POST_GET_REDIRECT_PATTERN" 

    else:
        u_form = UserUpdateForm(instance=request.user) 
        p_form = ProfileUpdateForm(instance=request.user.profile)

    #To pass this form into the template we create here a context(sort of API)
    context = {  
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context) #Passing context into template so that we can access that form

'''Post-Redirect-Get. The post / redirect / get pattern or PRG pattern is a
 development approach that prevents duplicate content when submitting forms
  and provides a more intuitive user interface.'''

