from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, FormView
from src.apps.accounts.forms import RegisterForm, LoginForm


def home(request):
    if request.user.is_authenticated:
        print('User : ', request.user.email)
    else:
        print("User : ", False)
    return render(request, 'home/index.html', {})



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/registration.html'
    success_url = '/'


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'


    def form_valid(self, form):
        request     = self.request
        email       = form.cleaned_data.get('email')
        password    = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:home_page')
        else:
            return redirect('home:registration')

        return super(LoginForm, self).form_invalid()
