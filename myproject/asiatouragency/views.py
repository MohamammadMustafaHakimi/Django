from django.shortcuts import render, redirect # redirect is a built in django function that redirects the user to any page you want
from django.http import HttpResponse
from .form import ContactForm
from .models import Tour
# Create your views here.

# def index(request): # it is going to take the request (GET, POST, DELETE, PATCH...)
# # by default the request is a GET request which retrieves data and renders them on the page
#     return HttpResponse("Asia Tours Agency") # the argument is what we render on the page
#     # traditionally we have to create templates folder, and then create index.html


# def index(request): # takes a request
#     tours = Tour.objects.all() # captures all of the tour objects that we create
#     context = {'tours':tours} # this is a context dictionary from  views to template
#     return render(request, 'tours/index.html', context) # we have to pass the context dictionary to the render function


def home_view(request):
    return render(request, 'tours/home.html')

# Define the contact_view function to handle the contact form
def contact_view(request):
    if request.method == "POST": # checking if the request is POST
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm() # if the method is not POST, we will be creating an empty form object
    context = {'form':form}
    return render(request, 'tours/contact.html',context)

# Define the contact_success_view function to handle the success page

def contact_success_view(request):
    return render(request, 'tours/contact_success.html')
