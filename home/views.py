from django.shortcuts import render
# from django.core.mail import send_mail

# Create your views here.

def HomeView(request):
    return render(request, 'index.html',{})


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


