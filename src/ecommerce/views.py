from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'title': 'Hello World!',
        'content': 'Welcome to home page.',
    }
    if request.user.is_authenticated:
        context['premium_content'] = 'a7aaaaaaaaaaaa'
    template = 'home_page.html'
    return render(request, template, context)


def about_page(request):
    context = {
        'title': 'About Page',
        'content': 'Welcome to about page.',
    }
    template = 'home_page.html'
    return render(request, template, context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact Us',
        'content': 'Welcome to contact page.',
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)

    template = 'contact/view.html'
    return render(request, template, context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    template = 'auth/login.html'
    return render(request, template, context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        print(new_user)

    template = 'auth/register.html'
    return render(request, template, context)