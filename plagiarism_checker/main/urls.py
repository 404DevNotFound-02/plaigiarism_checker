from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('check-plagiarism/', views.check_plagiarism, name='check_plagiarism'),
    path('history/', views.view_history, name='view_history'),
]