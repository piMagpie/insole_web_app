from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
# from django.contrib.users import User

def register(request):
    if request.method == 'POST': # POST request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # password = form.clean_data.get('password')
            return redirect('blog-home')
    else: # GET request
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# message.debug
# message.info
# message.success
# message.warning
# message.error