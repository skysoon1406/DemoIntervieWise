"""
URL configuration for InterviewerPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from . import views

app_name = "users" 

urlpatterns = [
    path('',views.index,name="index"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('sign_in/',views.sign_in,name="sign_in"),
    path('login/',views.create_session,name="login"),
    path('logout/',views.delete_session,name="logout"),
]
