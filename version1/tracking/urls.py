from django.urls import path
from .views import get_latest_location, index

urlpatterns = [
    path('', index, name='index'),
    path('latest-location/', get_latest_location, name='latest-location'),
]
