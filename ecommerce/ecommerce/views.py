from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm,LoginForm,RegisterForm

def home_page(request):

    context = {
       "title":"What is done in love, is done well",
      
       "brand_name":"eGogh"
       
    }   

    if request.user.is_authenticated:
      context["premium_content"] = "OH YEAAHHH"

    return render(request,"home_page.html",context)

def about_page(request):

  context = {
       "title":"About Page!",
      #  "content":"Welcome to the About Page"
    }

  return render(request,"home_page.html",context)

def contact_page(request):

  contact_form = ContactForm(request.POST or None)
  context = {
      
       "title":"What would life be if we had no courage to attempt anything?",
      #  "content":"Welcome to the Contact Page",
       "form": contact_form,
       
    }

  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  # if request.method == "POST":
  #   print(request.POST)
  #   print(request.POST.get('fullName'))
  #   print(request.POST.get('email'))
  #   print(request.POST.get('comment'))
  return render(request,"contact/view.html",context)

def login_page(request):
  form = LoginForm(request.POST or None)
  context = {
    "title":"Login Page!",
    "form" : form
  }
  
  # print(request.user.is_authenticated)
  if form.is_valid():
    print(form.cleaned_data)
    
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")

    user = authenticate(username=username, password=password)
    
    # print(request.user.is_authenticated)
    print(user)
    if user is not None:
      # print(request.user.is_authenticated)
      # A backend authenticated the credentials
      login(request,user)
      # context['form'] = LoginForm()
      print("User logged in")
      return redirect("/login")

    else:
          # No backend authenticated the credentials
      print("Error!")
        

  
  return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
  form = RegisterForm(request.POST or None)

  context = {
    "form" : form
  }

  if form.is_valid():
    print(form.cleaned_data)
    username = form.cleaned_data.get("username")
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password")
    
    new_user = User.objects.create_user(username,email,password)
    print(new_user)
  return render(request,"auth/register.html",context)

