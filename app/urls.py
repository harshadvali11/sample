from django.urls import path
from app import views
app_name='app'

urlpatterns=[
    path('temp/',views.temp,name='temp'),
]