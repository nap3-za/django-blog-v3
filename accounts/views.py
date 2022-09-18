from django.shortcuts import render, redirect, Http404
from .forms import RegForm, LoginForm, UpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Account
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.

def RegView(request, *args, **kwargs):
    form = RegForm(request.POST or None)
    if form.is_valid() and form != None:
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        surname = form.cleaned_data.get("surname")
        email = form.cleaned_data.get("email")
        phone_number = form.cleaned_data.get("phone_number")
        continent = form.cleaned_data.get("continent")
        password = form.cleaned_data.get("password")

        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
        account = Account.objects.create(user=user,
            first_name=first_name,
            surname=surname,
            phone_number=phone_number,
            email=email,
            continent=continent
        )

        login(request, user)
        return redirect("http://127.0.0.1:8000/")
    else:
        pass
    context = {'form': RegForm}
    return render(request, "accounts/reg.html", context)


def LoginView(request, *args, **kwargs):

    form = LoginForm(request.POST or None)
    if form.is_valid() and form != None:
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)

        else:
            pass

        return redirect("http://127.0.0.1:8000/")
    else:
        pass
    context = {'form': LoginForm}
    return render(request, "accounts/login.html", context)

@login_required
def LogoutView(request, *args, **kwargs):


    logout(request)
    return redirect("http://127.0.0.1:8000/")

@login_required
def MyAccView(request, *args, **kwargs):

    account = Account.objects.get(user=request.user)
    context = {"acc": account}
    return render(request, "accounts/myaccount.html", context)

@login_required
def UpdateAccView(request, *args, **kwargs):
    form = UpdateForm(request.POST or None)
    acc = Account.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)
    if form.is_valid() and form != None:
        first_name = form.cleaned_data.get("first_name")
        surname = form.cleaned_data.get("surname")
        email = form.cleaned_data.get("email")
        phone_number = form.cleaned_data.get("phone_number")
        continent = form.cleaned_data.get("continent")
    

        acc.first_name = first_name
        acc.surname = surname
        acc.email = email
        acc.phone_number = phone_number
        acc.continent = continent
        acc.save()
        print(acc.first_name)
        return redirect("http://127.0.0.1:8000/accounts/my-account/")
    else: 
        print("form is none")
    context = {"acc": acc, "user": user}
    return render(request, "accounts/update.html", context)


def DeleteAccountView(request, *args, **kwargs):

    acc = Account.objects.get(first_name=request.user.first_name)
    acc.delete()

    user = User.objects.get(first_name=request.user.first_name)
    user.delete()

    return redirect("http://127.0.0.1:8000/accounts/register/")


