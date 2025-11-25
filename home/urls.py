from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('request/', views.request_blood, name='request'),
    path('donate/', views.donate, name='donate'),
    path('about/', views.about, name='about'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('register-donor/', views.register_donor, name='register_donor'),
    path('profile/', views.profile, name='profile'),
    path('availability/', views.blood_availability, name='blood_availability'),
    path('types/', views.blood_types, name='blood_types'),
    path('search-donor/', views.search_donor, name='search_donor'),
    path('volunteer/', views.register_volunteer, name='register_volunteer'),
    path('stay-contact/', views.stay_contact, name='stay_contact'),

]
