from django.urls import path
from userapp import views

urlpatterns= [
    path('login/<email>/<password>/', views.login),
]