from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from contacts.models import Contacts
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, ': You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invald Username/Password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

    
def register(request):
    print(type(request))
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email ).exists():
                    tag = 'Click <a href="login">here</a>'
                    messages.error(request, 'Email is Already linked with another account, %s' % tag, extra_tags='html')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password
                    )
                    user.save()
                    messages.success(request, 'Registration successful, Log in now')
                    return redirect('login')

        else:
            messages.error(request, 'Password do not match')
            rd = redirect('register')
            rd.context = {'demo': 'This is demo'}
            return rd
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
    else:
        user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=0)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)