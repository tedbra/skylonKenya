from django.shortcuts import render, redirect
# from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Job
from .forms import ContactForm

# Create your views here.

def HomeView(request):
    return render(request, 'home.html',{})



class JobListView(ListView):

    model = Job
    ordering = ['-id']
    template_name = 'jobs.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JobListView, self).get_context_data(*args, **kwargs)
        return context 

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'

    def get_context_data (self, *args,**kwargs):
        context = super(JobDetailView, self).get_context_data(*args,**kwargs)
        return context


def process_footer_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("form is valid")
            return redirect(request.META.get('HTTP_REFERER'))  # Redirect back to the same page
        else:
            print("form is invalid: ", form.errors)
            return redirect(request.META.get('HTTP_REFERER'))  # Redirect back to the same page
    else:  # Handle GET requests if necessary
        return redirect('home')  # Or wherever you want to redirect