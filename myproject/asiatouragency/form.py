# file for creating forms
from django import forms # importing the builtin forms module/library of django

# main class for all of our forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) # multiline textbox

    def send_email(self):
        print(f"Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}") # cleaned data means that the form contains all the validate input data from the form
