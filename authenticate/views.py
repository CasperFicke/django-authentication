from django.shortcuts import render

# home view
def home(request):
  return render(request, 'authenticate/home.html', {})

# about view
def about(request):
  myfirst_name = 'Casper'
  mylast_name  = 'Ficke'
  context = {'first_name': myfirst_name, 'last_name': mylast_name}
  return render(request, 'authenticate/about.html', context)