from django.urls import path
from .views import article

app_name = 'tester'

urlpatterns = [
    path('', article ),
       
]