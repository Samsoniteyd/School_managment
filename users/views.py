from django.shortcuts import render,redirect
from . forms import CreateProfile, UpdateProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
# Create your views here.




def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

     form = CreateProfile()

    if request.method== 'POST':
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            

            if User.objects.filter(username=username).exists():
                messages.warning(request, "username already exist")
        
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.warning(request, "email already taken")
                
                return redirect('register')
            if password != password2:
                messages.warning(request, "password not match")
                   
                return redirect('register')

            user = User.objects.create_user(username,email,password) 
            form= form.save(commit=False)      
            form.user = user
            form.save()
            messages.success(request, "Registration successfull." + user)

            if 'next' in request.GET:
                next_url = request.GET.get('next')
                return redirect(next_url)
            
            # send_mail(
            #  subject= 'registered',
            #  message= f'{username} you have successfully registered',
            #  from_email= settings.EMAIL_HOST_USER,
            #  recipient_list = [email],
            #  fail_silently=False)
 
            return redirect('login')

        # form = CreateUserForm()
        # if request.method== 'POST':
        #     form = CreateUserForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         form.save()
        #         user = form.cleaned_data.get('username')
        #         messages.success(request, "Registration successfull." + user)
        #         return redirect('login')
    
    context={
        'form': form
    }
    return render(request, 'users/register.html', context)


#login page
#login page
def loginuser(request):

    
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('passwd')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "login successfull." + username )
            

            if 'next' in request.GET:
                next_url = request.GET.get('next')
                return redirect(next_url)
            
            return redirect('dashboard')
        else:
            messages.warning(request, "invalid user/password.")
            return redirect('login')


    return render(request, 'users/login.html')


def logoutuser(request):
    logout(request)
    messages.success(request, "logout successfull.")
    return redirect('login')

@login_required(login_url=('login'))
def dashboard(request):
    user = request.user.profile

    context= {
        'profile': user
    }
    return render(request, 'users/dashboard.html', context)





# update page
# update page


@login_required(login_url=('login'))

def update_profile(request):
    user = request.user.profile
    form = UpdateProfile(instance=user)

    if request.method == 'POST':
        forms = UpdateProfile(request.POST, request.FILES, instance=user)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')


    context= {
        'form': form
    }


    return render(request, 'users/update.html', context )
    