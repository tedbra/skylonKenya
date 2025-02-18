from django import forms
from .models import Job, Contact

class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = "__all__"

        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class':'contactus', 
                    'placeholder':'Your Name', 
                    'type':'text', 
                    'name':'Your Name',
                }
                ),
            'email' : forms.TextInput(attrs={'class':'contactus', 'placeholder':'Your Email', 'type':'text', 'name':'Your Email'}),
            'phone' : forms.TextInput(attrs={'class':'contactus', 'placeholder':'Phone Number', 'type':'text', 'name':'Your Phone'}),
            'message':forms.Textarea(attrs={'class':'textarea', 'placeholder':'Message', 'type':'text', 'name':'Message'}),
        }
