from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,DeleteView
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import TodoTable

from django.shortcuts import redirect

class HomePageView(LoginRequiredMixin,ListView):
    context_object_name = 'data'
    model = TodoTable
    template_name = 'baseApp/home.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = context['data'].filter(userName = self.request.user)
        return context
    

class LoginPageView(LoginView):
    template_name = 'baseApp/login.html'

    def post(self, request, *args, **kwargs):
        username = self.request.POST['uName']
        password = self.request.POST['pWord']
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('base:homePage')
        #return super().post(request, *args, **kwargs)

class LogOutView(LoginRequiredMixin,LogoutView):
    next_page = 'base:login'
    
            

class RegisterPageView(CreateView):
    template_name = 'baseApp/register.html'
    form_class = UserCreationForm
    #success_url = reverse_lazy('base:login')

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        email = self.request.POST['email']
        firstName = self.request.POST['firstName']
        lastName = self.request.POST['lastName']
        user = User.objects.create_user(username, password=password, first_name=firstName, last_name=lastName,email=email)
        user.save()
        return redirect('base:login')
        #return super().post(request, *args, **kwargs)

class CreatePageView(LoginRequiredMixin,CreateView):
    template_name = 'baseApp/add.html'
    model = TodoTable
    fields = "__all__"
    #success_url = reverse_lazy('base:homePage')
    def post(self, request, *args, **kwargs):
        userName = request.user
        topic = self.request.POST['topic']
        desc = self.request.POST['description']
        data = TodoTable(userName = userName, title = topic,description=desc)
        data.save()
        return redirect('base:homePage')
        #return super().post(request, *args, **kwargs)       

class DisplayPageView(LoginRequiredMixin,DetailView):
    template_name = 'baseApp/display.html'
    model = TodoTable
    context_object_name = 'data'

class DeleteDataView(LoginRequiredMixin,DeleteView):
    model = TodoTable
    context_object_name = 'data'
    template_name = 'baseApp/deleteConfirm.html'
    success_url = reverse_lazy('base:homePage')
