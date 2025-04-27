from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django .contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from .models import Admin, Item, Supplier, Category
from django.contrib.auth.hashers import make_password

class Index(TemplateView):
    template_name = 'apps/index.html'

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'apps/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            hashed_password = make_password(password)

            Admin.objects.create(username=username, password=hashed_password)
            
            return redirect('index')
        
        return render(request, 'apps/register.html', {'form': form})
