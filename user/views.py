from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView


from .forms import RegisterForm
from .models import UserProfile
from blog.views import BasicView
from .forms import ProfileUpdateForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class LoginView(BasicView, View):
    def get(self, request):
        context = {}
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username yoki password xato!')
            return redirect('login')

class Profile(View):
    def get(self, request):
        username = request.user.username
        user = UserProfile.objects.get(username=username)
        context = {
            'user':user
        }
        return render(request, 'profile.html', context)

class ProfileUpdate(UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')