from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import SignUpForm

# home view
def home(request):
  return render(request, 'authenticate/home.html', {})

# about view
def about(request):
  myfirst_name = 'Casper'
  mylast_name  = 'Ficke'
  context = {'first_name': myfirst_name, 'last_name': mylast_name}
  return render(request, 'authenticate/about.html', context)

# register view
def register_user(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(request, username=username, password=password)
      login(request, user)
      messages.success(request, ("You're logged in"))
      return redirect('home')
  else:
    form = SignUpForm()
  
  context = {'form': form}
  return render(request, 'authenticate/register.html', context)


# login view
def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, ("You're logged in"))
      return redirect('home')
    else:
      messages.success(request, ("Invalid username or password!"))
      return redirect('login')
  else:
    return render(request, 'authenticate/login.html', {})

# logout view
def logout_user(request):
    logout(request)
    messages.success(request, ("You're logged out"))
    return redirect('home')