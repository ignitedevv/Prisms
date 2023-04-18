from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm, RegistrationForm
import datetime
from django.contrib.auth import login as djlogin
import random

# Create your views here.
def home(request):
    return render(request,'MainWebsite/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            created_user_id = random.randint(100000000000,999999990000)
            user.user_id = created_user_id
            user.username = created_user_id
            user.set_password(form.cleaned_data['password'])
            print(user.password)
            user.last_login = datetime.datetime.now()
            user.save()
            djlogin(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
        form = RegistrationForm(request.POST, request.FILES)

    context = {
        "form": form,

    }

    return render(request, 'MainWebsite/register.html', context=context)

# Login for student
class LoginUser(LoginView):

    from django.contrib.auth.hashers import check_password




    template_name = 'MainWebsite/login.html'
    form_class = LoginUserForm
    print('test234234234234234234234')


# Logout Page
def logout(request):
    auth.logout(request)
    return render(request, 'MainWebsite/index.html')

def dashboard(request):
    return render(request, 'prisms/dashboard.html')