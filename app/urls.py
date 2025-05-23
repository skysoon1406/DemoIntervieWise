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
from app import views

app_name = "pages"

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('payment/',views.payment,name="payment"),
    path('create_purchase/',views.create_purchase,name="create_purchase"),
]
