from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): # it is going to take the request (GET, POST, DELETE, PATCH...)
# by default the request is a GET request which retrieves data and renders them on the page
    return HttpResponse("Asia Tours Agency") # the argument is what we render on the page
    # traditionally we have to create templates folder, and then create index.html
