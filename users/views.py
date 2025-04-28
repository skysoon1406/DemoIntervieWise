from django.shortcuts import render,redirect
from .forms import  UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def sign_up(request):
    form = UserCreationForm
    return render(
        request,
        'users/sign_up.html',
        {"form":form}
        )

def index(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        form.save()

        return redirect("pages:home")
    
def sign_in(request):
    next = request.GET.get("next",reverse("pages:home"))
    return render(
        request,
        'users/sign_in.html',
        {"next":next}
        )

def create_session(request):  # 登入session
    if request.POST :
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST['username']
        # password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None: 
            login(request,user)
            next =  request.POST.get("next",reverse("pages:home"))
            messages.success(request,"登入成功")  # flash messages
            return redirect(next)
        else: 
            return redirect("users:sign_in")

@require_POST        
def delete_session(request):
    logout(request)
    messages.success(request,"已登出")
    return redirect("pages:home")
