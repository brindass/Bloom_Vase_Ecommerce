from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def test(request):
    form = CreateUserForm()
    context = {'form':form}
    return render(request,'user/test.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form_data =request.POST.copy()
        form = CreateUserForm(form_data)
        if form.is_valid() :
            form.save()
            return redirect('login')
    context = {'form':form}  
    return render(request,'user/register.html',context)    

def user_login(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print("user not found")
            return redirect('user_login')
    return render(request,'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')



@never_cache
def home(request):
    if request.user.is_authenticated:
        return render(request,'product/home.html')
    return redirect('user_login')


# @never_cache
# def loginpage(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
            
#             user = authenticate(request, username = username, password = password)
#             if user is not None:
#                 login(request,user)
#                 # request.session['username'] = username
#                 return redirect('home')
#             else:
#                 messages.error(request,"Invalid username or password")
#                 return redirect('login')
#         return render(request,'login.html')
    
#     return redirect('home')

# def signup_page(request):
#      if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['firstname']
#         password = request.POST['password']
#         password1= request.POST['password1']
#         email    = request.POST['email']

#         if password == password1:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already exists')
#                 return redirect('signup')
#             else:
#                 user = User.objects.create_user(username, email, password)
#                 user.first_name = first_name
#                 user.save()
#                 messages.success(request, 'You have successfully signed up!')
#                 return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('signup')
    
#      else:
#          return render(request,'signup.html')