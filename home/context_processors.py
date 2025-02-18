# context_processors.py (create this file in your app)
from .forms import ContactForm  # Your form

def contact_form(request):
    return {'contact_form': ContactForm()}  # Create a new form instance