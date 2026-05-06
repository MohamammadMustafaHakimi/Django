from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required # special function that modify the behaviour of other function without changing the original functions
from django.contrib.auth.mixins import LoginRequiredMixin# simply reuseable classes that simply add specific functionality to class based views without being the primary class
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm
# note: class based views and function based views are the same, where one uses functions and the other uses classes

def register_view(request):
    if request.method == "POST": # checking if the user is submitting the registration form data
        form = RegisterForm(request.POST) # binds the POST data to your registration form
        if form.is_valid(): # validates the form against the rules in RegisterFrom. e.g is does the email have @
            username = form.cleaned_data.get("username") # extracts the username
            password = form.cleaned_data.get("password") # extracts the password
            user = User.objects.create_user(username=username, password=password) # create and hash the user's password in the database where the key is the username
            login(request, user) # auto log in
            return redirect('home') # redirect the user to the homepage after loging-in
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


    # checking if the request POST or not

def login_view(request):
    error_message = None
    if request.method == 'POST': # only processes authentication if form data is sent
        username = request.POST.get("username") # get's the username from the form
        password = request.POST.get("password") # get's the password from the form
        user = authenticate(request, username=username, password=password) # checks the credential against the database, and returns a user object if they are correct
        if user is not None: # if the verification is successful, as mentioned and a user object is returned (not empty)
            login(request, user) # get logged in
            next_url = request.POST.get('next') or request.GET.get('next') or 'home' # default is the home, but also checks where the user wants to go
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'accounts/login.html', {'error': error_message})  # if the password is wrong then the error message is rendered in the login page

def logout_view(request): # easiest function to write in authentication
    if request.method == "POST": # clears the user's session
        logout(request) # log the user out
        return redirect('login') # reidrects them to login page
    else: # if the request is a GET request we get redirected to home page
        return redirect('home')


# Home View, using the Decorator

@login_required # decorator which wraps home_view, and checks if the user is logged n weeeeeeeeee
def home_view(request): # only if the user is logged in then we want to keep them in the home view
    return render(request, 'auth1_app/home.html')

# Protected View: a view only for logged in users
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to' # ''next' - to reidrect URL

    def get(self, request):
        return render(request, 'registration/protected.html')
