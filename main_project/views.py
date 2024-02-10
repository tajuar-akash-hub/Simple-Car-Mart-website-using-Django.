from django.shortcuts import render,redirect
from . forms import Registration_form,change_user_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse
import requests
from posts.models import brand_model,car_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def home(request,car_brand_name_slug=None):

    Car_model_details = car_model.objects.all()  #all object from car model(name,price,brand_name)

    if car_brand_name_slug is not None:
        car_brand_slug_field= brand_model.objects.get(slug = car_brand_name_slug) #getting object

        print("printing this slug field",car_brand_name_slug)
        Car_model_details  = car_model.objects.filter(car_brand_name = car_brand_slug_field)
        print("car model detials",Car_model_details)
        
    brand_model_details_all = brand_model.objects.all() #getting all data fron brand model(toyota, nissan etc)

    return render(request,"home.html",{'Car_model_details':Car_model_details,'brand_model_details_all':brand_model_details_all})



def signup(request):
    if request.method == "POST":
        form = Registration_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Registration_form()
    return render(request,"signup_page.html",{'form':form})

# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name,password=user_pass)
#             if user is not None:
#                 login(request,user)
#                 return redirect("profile_page")
#     else:
#         form = AuthenticationForm()
#     return render(request,"login.html",{'form':form})

class user_login_view(LoginView):
    template_name="login.html"

    def form_valid(self, form):
        response= super().form_valid(form)
        return response
    
    def form_invalid(self, form):
        response=  super().form_invalid(form)
        return response
    
    def get_success_url(self) -> str:
        return reverse_lazy("profile_page")

def profile_page(request):
    user_info = request.user
    context= {
        'user':user_info,
        'email':request.user.email
    }
    return render(request,"profile.html",context)
    

def edit_profile(request):
    if request.method == "POST":
        form = change_user_data(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_page")
    else:
        form = change_user_data(instance = request.user)
    return render(request,"update_profile.html",{'form':form})

# def show_user_info(request):
    
#     return render(request,"profile.html",{'user_info':user_info})

# def experiment_pass(request):
#     url = "http://127.0.0.1:8000/experiment_pass/"
#     response = requests.get(url)
#     print("he is the resut")
#     print(response.text)
#     # print("here is the result")
#     # print(request.GET)
#     # return render(request,"experiment_pass.html")

# def update_password(request):
#     if request.method == "POST":
#         form = SetPasswordForm(user = request.user,data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request,form.user)
#             return redirect("profile_page")
#     else:
#         form = SetPasswordForm(user=request.user)
#     return render(request,"password_change.html",{'form':form})

@method_decorator(login_required,name='dispatch')
class update_passwordview(PasswordChangeView):
    template_name='password_change.html'
    form_class=SetPasswordForm
    success_url = reverse_lazy("profile_page")


def user_logout(request):
    logout(request)
    return redirect("login_page")












        