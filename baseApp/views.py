from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import TodoTable

from django.shortcuts import render,redirect

class HomePageView(ListView):
    context_object_name = 'data'
    model = TodoTable
    template_name = 'baseApp/home.html'

class DisplayPageView(DetailView):
    template_name = 'baseApp/display.html'
    model = TodoTable
    context_object_name = 'data'

class LoginPageView(TemplateView):
    template_name = 'baseApp/login.html'

class RegisterPageView(CreateView):
    template_name = 'baseApp/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('base:login')

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        email = self.request.POST['email']
        firstName = self.request.POST['firstName']
        lastName = self.request.POST['lastName']
        user = User.objects.create_user(username, password=password, first_name=firstName, last_name=lastName,email=email)
        user.save()
        return super().post(request, *args, **kwargs)

        
class UpdatePageView(UpdateView):
    template_name = 'baseApp/update.html'

class CreatePageView(CreateView):
    template_name = 'baseApp/add.html'
    model = TodoTable
    fields = "__all__"
    def post(self, request, *args, **kwargs):
        userName = request.user
        topic = self.request.POST['topic']
        desc = self.request.POST['description']
        data = TodoTable(userName = userName, title = topic,description=desc)
        data.save()
        return super().post(request, *args, **kwargs)
    success_url = reverse_lazy('base:homePage')    
        
class DeleteDataView(DeleteView):
    model = TodoTable
    context_object_name = 'data'
    template_name = 'baseApp/deleteConfirm.html'
    success_url = reverse_lazy('base:homePage')


