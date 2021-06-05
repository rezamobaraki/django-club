from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from accounts.forms import UserRegistrationForm, UserLoginForm


class UserRegister(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(data['username'], data['email'], data['password'])
            messages.success(request, 'you registered successfully', 'info')
            return redirect('core:home')
        return render(request, self.template_name, {'form': form})


class UserLogin(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = 'accounts/login.html'
        self.form_class = UserLoginForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you are logged in successfully', 'info')
                return redirect('core:home')
            messages.error(request, 'username or password is wrong', 'warning')
        return render(request, self.template_name, {'form': form})
