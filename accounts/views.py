from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from accounts.forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponseBadRequest

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "accounts/login-form.html", {"form":form, "title": title})


def register_view(request):
    if not request.user.is_authenticated():
        print(request.user.is_authenticated())
        next = request.GET.get('next')
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect("/")

        context = {
            "form": form
        }
        return render(request, "accounts/register-form.html", context)
    else :
        # user stays on the same page, no activity
        return redirect('posts:list')

def logout_view(request):
    logout(request)
    return redirect("/")
