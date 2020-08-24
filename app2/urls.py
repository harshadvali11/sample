from django.urls import path
from app2 import views
app_name='app2'

urlpatterns=[
    path('app2_temp/',views.app2_temp,name='app2_temp'),
]