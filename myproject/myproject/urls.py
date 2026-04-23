"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# this acts as the url dispatcher
# basically it maps the URLs to the corresponding views functions or classes

from django.contrib import admin
from django.urls import path, include
# another urls.py should be created for the application folder; for each new application you need a new url.py file
urlpatterns = [
    path("admin/", admin.site.urls), # later in the project we will be adding more paths here, which routes the user to the correct view
    path('', include('asiatouragency.urls'))
]
