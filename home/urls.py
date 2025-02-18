
from django.urls import path
#from . import views 
from .views import HomeView, JobListView, JobDetailView, process_footer_contact


urlpatterns = [
    path('', HomeView, name='home'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:pk>', JobDetailView.as_view(), name='job-detail'),
    path('process_footer_contact/', process_footer_contact, name='process_footer_contact'),
]