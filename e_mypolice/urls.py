from django.contrib import admin
from django.urls import path
from e_mypolice import views

urlpatterns = [
    path('',views.index),
    path('contact',views.contact),
    path('services',views.services),
    path('logout', views.logout),
    path('fir',views.fir),
    path('missingperson',views.missingperson),
    path('stolen',views.stolen),
    path('police',views.police),

]
