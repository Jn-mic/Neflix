from django import views
from django.shortcuts import render
from django .views import View

# Create your views here.
# AUTH_USER.MODE='Movies'.CustomerUSER

class Home(views):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')

