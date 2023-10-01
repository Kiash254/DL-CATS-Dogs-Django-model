from django.urls import path
from .views import Predict

app_name='predctive_model'

urlpatterns=[
    path('',Predict,name='home')
]