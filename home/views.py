from django.shortcuts import render
# from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Job

# Create your views here.

def HomeView(request):
    return render(request, 'home.html',{})


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         send_mail(
#             'Contact Form Submission',  # Subject
#             f'Name: {name}\nEmail: {email}\nMessage: {message}',  # Message
#             'skyloneducation@gmail.com',  # From (Your website's sending email)
#             ['skyloneducation@gmail.com'],  # To (Your email address)
#             fail_silently=False,  # Set to True for production to avoid errors
#         )
#         #return render(request, 'contact_success.html') # Redirect to a success page
#         return JsonResponse({'status' : 'success'})
#     return render(request, 'index.html')  # Render the contact form


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
    