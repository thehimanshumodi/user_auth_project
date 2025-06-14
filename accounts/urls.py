from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/patient/', views.patient_dashboard_view, name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard_view, name='doctor_dashboard'),
    path('', views.login_view, name='home'), # Default home page is login
]