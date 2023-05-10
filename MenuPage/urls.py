from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_mailing/', views.landing, name='landing')
]
