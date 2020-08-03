from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
from account.forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank You For Joining Us")
            return redirect('login')
        else:
            messages.error(request, "Invalid Information")
            return render(request, "account/register.html", {'form': form})
    else:
        form = UserRegistrationForm(request.POST)
    return render(request, "account/register.html", {'form': form})
    # first_name = request.POST['first_name']
    # last_name = request.POST['last_name']
    # user_name = request.POST['user_name']
    # email = request.POST['email']
    # password = request.POST['password']
    # password2 = request.POST['password2']
    #
    #     if password == password2:
    #         if User.objects.filter(username=user_name).exists():
    #             messages.error(request, "that user name is already taken")
    #             return redirect('register')
    #         else:
    #             if User.objects.filter(email=email).exists():
    #                 messages.error(request, "that email is already taken")
    #                 return redirect('register')
    #             else:
    #                 user = User.objects.create(username=user_name, password=password, email=email,
    #                                            first_name=first_name,
    #                                            last_name=last_name, )
    #                 # auth.login(request, user)
    #                 # messages.success(request, "you are now logged in ")
    #                 # return redirect("index")
    #                 user.save()
    #                 messages.success(request, "Thank You For Joining Us")
    #                 return redirect('login')
    #     else:
    #         messages.error(request, "Passwords do not match")
    #         return redirect('register')
    # else:
    #     return render(request, "account/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in ")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Information")
            return redirect('login')

    return render(request, "account/login.html")


@login_required()
def dashboard(request):
    return render(request, "account/dashboard.html")


def logout(request):
    return redirect('index')
