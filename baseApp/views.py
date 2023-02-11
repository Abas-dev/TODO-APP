from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name = 'baseApp/home.html'

class LoginPage(TemplateView):
    template_name = 'baseApp/login.html'

class RegisterPage(TemplateView):
    template_name = 'baseApp/register.html'

class UpdatePage(TemplateView):
    template_name = 'baseApp/update.html'