from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def special(request):
    return HttpResponse("Logged in.")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse("Compte inactive.")
        else:
            print("Quelqu'un essaye de se connecter et a echoué. \nUsername: {}\nPassword: {}".format(username, password))
            return HttpResponse("Login Invalid.")
    else:
        return render(request, 'login.html', {})

@login_required
def live_search(request):
    return render(request, 'live_search.html', {})