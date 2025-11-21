from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('request/', views.request_blood, name='request'),
    path('donate/', views.donate, name='donate'),
    path('about/', views.about, name='about'),
    path('login/', views.login_page, name='login'),

]
