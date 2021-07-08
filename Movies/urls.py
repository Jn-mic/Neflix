from django.urls import path

from .import views
from . views import Home

app_name='Movies'

urlpatterns=[
    path('',Home.as_views()),
]