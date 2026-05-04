from django.urls import path
# views should be imported for mapping to that index function inside it, where the index funciton returns an HTTP response with Asia Tours Agency rendered on the page
from . import views


# Define a list of url patterns

# urlpatterns = [
#     path('', views.index) # we imported this on the top of this page; it takes two arguments, namely route, and view
# ]

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success', views.contact_success_view, name='contact-success')
]
