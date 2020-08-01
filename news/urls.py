from django.urls import path
from news import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('hindustantimes/',views.hindustantimes,name  = 'hindustan')
]
