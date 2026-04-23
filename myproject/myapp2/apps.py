from django.apps import AppConfig

# this file contains the configuration class for your application

# the below class is particularly useful for pluggable applications, because it allows to specify meta data or configuration hooks
class Myapp2Config(AppConfig):
    name = "myapp2" # the name is the same as the name of the foler on the right (of the actual application)
